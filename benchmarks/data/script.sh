#!/bin/sh

echo "Benchmark 1: Compare power consumed | Started"

# Measure node power in empty cluster 
python3 script.py -c "import script; script.get_node_power()"

# Deploy workload
kubectl apply -f ../peaks_deployment/pod.yaml;

# Measure node power cluster 
python3 script.py -c "import script; script.get_node_power()"

# Remove workload
kubectl delete -f ../peaks_deployment/pod.yaml;

# Measure node power in empty cluster 
python3 script.py -c "import script; script.get_node_power()"

# Deploy peaks 
kubectl apply -f ../peaks_deployment/peaks_crd.yaml;
kubectl apply -f ../peaks_deployment/deployment.yaml;
kubectl apply -f ../peaks_deployment/pod.yaml;

# Measure node power cluster 
python3 script.py -c "import script; script.get_node_power()"

echo "Benchmark 1: Compare power consumed | Completed"

echo "Benchmark 2: Compare cpu utilization | Started"

