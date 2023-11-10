package energyefficientscheduling

import (
	"fmt"
	"math"
	"context"

	v1 "k8s.io/api/core/v1"
	"k8s.io/apimachinery/pkg/runtime"
	"k8s.io/kubernetes/pkg/scheduler/framework"
	"github.com/paypal/load-watcher/pkg/watcher"

	pluginConfig "sigs.k8s.io/scheduler-plugins/apis/config"
	"sigs.k8s.io/scheduler-plugins/apis/config/v1beta2"
)

cconst (
	Name = "Peaks"
)

type Peaks struct {
	handle         framework.Handle
	collector      *Collector
	args           *config.PeaksArgs
}

type PowerModel struct {
	K0 float64
	K1 float64
	K2 float64
	// Power = K0 + K1 * e ^(K2 * x) : where x is utilisation
}

var _ framework.ScorePlugin = &Peaks{}

func (pl *Peaks) Name() string {
	return Name
}

func New(obj runtime.Object, handle framework.Handle) (framework.Plugin, error) {
	fmt.Printf("Input config %+v\n", obj)

	args, ok := obj.(*config.PeaksArgs)
	if !ok {
		return nil, fmt.Errorf("want args to be of type PeaksArgs, got %T", obj)
	}
	collector, err := NewCollector(&args.WatcherAddress)
	if err != nil {
		return nil, err
	}
	pl := &Peaks{
		handle: handle,
		collector: collector,
		args: args,
	}
	return pl, nil
}

func (pl *Peaks) Score(ctx context.Context, cycleState *framework.CycleState, pod *v1.Pod, nodeName string) (int64, *framework.Status) {
	score := framework.MinNodeScore

	nodeInfo, err := pl.handle.SnapshotSharedLister().NodeInfos().Get(nodeName)
	if err != nil {
		return score, framework.NewStatus(framework.Error, fmt.Sprintf("getting node %q from Snapshot: %v", nodeName, err))
	}

	metrics, _ := pl.collector.GetNodeMetrics(nodeName)
	if metrics == nil {
		fmt.Println("Failed to get metrics for node; using minimum score", "nodeName", nodeName)
		return score, nil
	}

	var curPodCPUUsage int64
	for _, container := range pod.Spec.Containers {
		curPodCPUUsage += PredictUtilisation(&container)
	}
	if pod.Spec.Overhead != nil {
		curPodCPUUsage += pod.Spec.Overhead.Cpu().MilliValue()
	}
	fmt.Println("Pod cpu usage predicted ", curPodCPUUsage)

	var nodeCPUUtilPercent float64
	var cpuMetricFound bool
	for _, metric := range metrics {
		if metric.Type == watcher.CPU {
			if metric.Operator == watcher.Average || metric.Operator == watcher.Latest {
				nodeCPUUtilPercent = metric.Value
				cpuMetricFound = true
			}
		}
	}

	if !cpuMetricFound {
		fmt.Println("Cpu metric not found in node metrics for nodeName", nodeName)
		return score, nil
	}

	nodeCPUCapMillis := float64(nodeInfo.Node().Status.Capacity.Cpu().MilliValue())
	nodeCPUUtilMillis := (nodeCPUUtilPercent / 100) * nodeCPUCapMillis

	var predictedCPUUsage float64
	if nodeCPUCapMillis != 0 {
		predictedCPUUsage = 100 * (nodeCPUUtilMillis + float64(curPodCPUUsage)) / nodeCPUCapMillis
	}

	if predictedCPUUsage > 100 {
		return score, framework.NewStatus(framework.Success, "")
	} else {
		jump_in_power := getPowerJumpForUtilisation(nodeCPUUtilPercent, predictedCPUUsage, getPowerModel(nodeName))
		// Here i just assume max power that a node can consume is 500... will fix this ~@felix
		return int64((500 - jump_in_power) / 500), framework.NewStatus(framework.Success, "")
	}
}

func (pl *Peaks) ScoreExtensions() framework.ScoreExtensions {
	return pl
}

func (pl *Peaks) NormalizeScore(context.Context, *framework.CycleState, *v1.Pod, framework.NodeScoreList) *framework.Status {
	return nil
}

func PredictUtilisation(container *v1.Container) int64 {
	if _, ok := container.Resources.Requests[v1.ResourceCPU]; ok {
		return int64(math.Round(float64(container.Resources.Requests.Cpu().MilliValue())))
	} else if _, ok := container.Resources.Limits[v1.ResourceCPU]; ok {
		return container.Resources.Limits.Cpu().MilliValue()
	} else {
		return v1beta2.DefaultRequestsMilliCores
	}
}

func getPowerJumpForUtilisation(x, p float64, m PowerModel) float64 {
	return m.K1 * (math.Exp(m.K2*p) - math.Exp(m.K2*x))
}

func getPowerModel(nodeName string) PowerModel {
	if nodeName == "10.242.64.10" {
		return PowerModel{371.7412504314313, -91.50493019588365, -0.03186049052516228}
	}
	return PowerModel{371.7412504314313, -91.50493019588365, -0.05186049052516228}
}