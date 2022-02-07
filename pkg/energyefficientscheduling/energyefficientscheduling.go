package energyefficientscheduling

import (
	"context"

	v1 "k8s.io/api/core/v1"
	"k8s.io/apimachinery/pkg/runtime"
	"k8s.io/kubernetes/pkg/scheduler/framework"
)

const Name = "EnergyEfficientScheduling"

type Epic struct{}

var _ framework.ScorePlugin = &Epic{}

func (pl *Epic) Name() string {
	return Name
}

func New(_ runtime.Object, _ framework.Handle) (framework.Plugin, error) {
	return &Epic{}, nil
}

func (pl *Epic) Score(ctx context.Context, state *framework.CycleState, pod *v1.Pod, nodeName string) (int64, *framework.Status) {
	return 0, nil
}

func (pl *Epic) ScoreExtensions() framework.ScoreExtensions {
	return pl
}

func (pl *Epic) NormalizeScore(ctx context.Context, state *framework.CycleState, pod *v1.Pod, scores framework.NodeScoreList) *framework.Status {
	return nil
}
