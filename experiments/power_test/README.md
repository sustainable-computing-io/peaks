# Power Consumption Monitoring and Analysis with IPMI

## Overview

This test involves monitoring the power consumption of a Kubernetes cluster while running a stress-ng workload. We utilized the IPMI (Intelligent Platform Management Interface) tool to measure and aggregate instantaneous power consumption across three nodes: control-plane, kind-worker1, and kind-worker2.

## Objectives

Monitor Instantaneous Power Consumption:

- We employed the ipmitool to continuously monitor the instantaneous power usage of the nodes in the cluster. The readings were captured in real-time to analyze the power impact of the workloads running on the cluster.

Aggregate Power Consumption:

- Power readings from each node were aggregated over the monitoring period to provide a comprehensive view of the total power consumed by the cluster during the test.

Scale the Workload:

- We scaled the stress-ng pod to 120 replicas using Kubernetes' default and peak scheduling capabilities. This allowed us to simulate a heavy workload and assess its impact on power consumption.

Comparison of Power Consumption:

- The aggregated power consumption was compared across the three nodes `control-plane`, `kind-worker1` and `kind-worker2`. The `control-plane` is taninted for `NoSchedule` so the pods will be placed only on `kind-worker1` and `kind-worker2`
This comparison helped us understand how the total power consumption (and hence savings) of cluster when Peaks was used vs when default scheduler was used.

## Pre-requisite

Make sure the dependencies are installed on the worker nodes.

### Install dependencies

```bash
sudo dnf install -y sudo dnf install -y gnuplot
sudo dnf install -y ipmitool
```

For most modern Linux distributions, the IPMI driver should be included in the kernel, but you can manually load it using the following command:

```bash
sudo apt-get install ipmitool   # For Ubuntu/Debian
sudo yum install ipmitool       # For CentOS/RHEL
```

To check if the modules are loaded and after loading the modules, check if the device files are created:

```bash
lsmod | grep ipmi
ls /dev/ipmi*
```

### Monitor Power on the worker nodes

```sh
./monitor_power.sh
```

Now apply the deployment to monitor power when default scheduler is used:

```sh
kubectl apply -f default_sng.yaml
kubectl scale deployment default-stress-ng --replicas=30
kubectl scale deployment default-stress-ng --replicas=60
kubectl scale deployment default-stress-ng --replicas=90
kubectl scale deployment default-stress-ng --replicas=120
#kubectl scale deployment default-stress-ng --replicas=150
```
Repeat the experiment with `peaks_sng.yaml`


