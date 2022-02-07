package main

import (
	"math/rand"
	"os"
	"time"

	"k8s.io/component-base/logs"
	"k8s.io/kubernetes/cmd/kube-scheduler/app"

	scheduling "github.com/sustainable-computing-io/epic/pkg/energyefficientscheduling"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	command := app.NewSchedulerCommand(app.WithPlugin(scheduling.Name, scheduling.New))
	logs.InitLogs()
	defer logs.FlushLogs()

	if err := command.Execute(); err != nil {
		os.Exit(1)
	}
}
