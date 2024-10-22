# Getting Started

## Run `stress-ng` workload to stress the nodes with 100% CPU Utilization.
```sh
git clone https://github.com/husky-parul/peaks.git; cd peaks; git fetch origin -a; git checkout -b benchmarks origin/benchmarks;

# If you want to be able to schedule pods on the Kubernetes control-plane node, you need to remove a taint on the master nodes.

kubectl taint nodes --all node-role.kubernetes.io/master-
kubectl taint nodes --all  node-role.kubernetes.io/control-plane-

kubectl apply -f stress-ng/stress-ng-deployment.yaml 

$ configmap/stress-ng-config created
$ daemonset.apps/stress-ng-daemonset created

```

## Get metrics from Prometheus

### Prometheus Configuration Settings
The configmap `prometheus-query-config` configures container to query Prometheus 

```sh
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-query-config
data:
  # Prometheus server URL
  PROMETHEUS_URL: "http://prometheus-k8s.monitoring.svc.cluster.local:9090/api/v1/query_range"

  # Start and end times for querying Prometheus
  START_TIME: "2024-09-31T10:00:00Z"
  END_TIME: "2024-10-03T10:00:00Z"

  # Directory to store the CSV files (mounted from PVC)
  CSV_DIRECTORY: "/mnt/pvc/"

  # List of metrics to query, as a comma-separated string
  METRICS_LIST: 'kepler_node_dram_joules_total,kepler_node_other_joules_total,kepler_node_package_joules_total,kepler_node_platform_joules_total,node_cpu_seconds_total'

  # Optional: Query interval (time between queries in seconds)
  QUERY_INTERVAL: "60"

```

Edit and save `prometheus-query-configmap.yaml` 

The PVC defined in `./prometheus-query/prometheus-pvc.yaml` is used to save the metrics in a csv file

To deploy the `prometheus-query` container

```sh
kubectl apply -f ./prometheus-query/prometheus-query-configmap.yaml

kubectl apply -f ./prometheus-query/prometheus-pvc.yaml

kubectl apply -f ./prometheus-query/prometheus-query-deployment.yaml
```
