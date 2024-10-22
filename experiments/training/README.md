# Set up #

## Docker environment ##
```
git clone https://github.com/husky-parul/kepler.git 
cd kepler
git fetch origin -a
git switch -c local-dev origin/local-dev-docker-compose 
cd ..
cd peaks/experiments/training
docker compose up `

```

Ensure the setup works by:
* Attach a shell to the training-prom_reader container (``` docker exec -it training-prom_reader-1 bash ```)
* look in the data folder (```ls data```), and ensure the specificed metrics (in the metrics.properties file) have filed associated with them 
    * The contents of these files should have the metrics for the specified metric name


## Kubernetes environment: ##

Prerequisite:
Must have Kepler and Promtheus monitoring running (this runs on the Kepler kind-worker node)

```
cd peaks/experiments/training

docker exec kind-worker sh -c "mkdir /mnt/data"
docker exec kind-worker sh -c "echo 'Hello from Kubernetes storage' > /mnt/data/index.html"

kubectl apply -f pv.yaml
kubectl apply -f save_metrics_deployment.yaml

```
Ensure the setup works by:
* check the pod is running (``` kubectl get pods ```)
* copy the name of the pod and check the logs of the pods to see which metrics have saved (``` kubectl logs <name_of_pod> ```)
* check that the metrics are saved in the PVC 

```
kubectl exec --stdin --tty <name_of_pod> -- /bin/bash 

cd /mnt/data/storage
ls

```
