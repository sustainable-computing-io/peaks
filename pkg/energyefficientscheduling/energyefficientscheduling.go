package energyefficientscheduling

import (
	"context"

	v1 "k8s.io/api/core/v1"
	"k8s.io/apimachinery/pkg/runtime"
	"k8s.io/klog"
	"k8s.io/kubernetes/pkg/scheduler/framework"
)

const Name = "Peaks"

type Peaks struct{}

var _ framework.ScorePlugin = &Peaks{}

func (pl *Peaks) Name() string {
	return Name
}

func (pl *Peaks) Score(ctx context.Context, state *framework.CycleState, pod *v1.Pod, nodeName string) (int64, *framework.Status) {
	return 0, nil
}

func (pl *Peaks) ScoreExtensions() framework.ScoreExtensions {
	return pl
}

func (pl *Peaks) NormalizeScore(ctx context.Context, state *framework.CycleState, pod *v1.Pod, scores framework.NodeScoreList) *framework.Status {
	return nil
}

func New(_ runtime.Object, handle framework.Handle) (framework.Plugin, error) {

	klog.V(3).Infof("Peaks")

	return &Peaks{}, nil
}
