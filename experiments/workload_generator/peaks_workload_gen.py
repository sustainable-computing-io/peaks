from kubernetes import client, config, dynamic
import yaml
import time
from datetime import datetime

ENVIRONMENT = 'local'
DEPLOYMENT_NAME = "cpu-stress-test"
NAMESPACE = "felix"
MAX_INSTANCES = 10
SCALE_UP_DURATION = 300

def create_client(environment):
	if environment == 'local':
		c = config.load_kube_config()
	if environment == 'cloud':
		c = config.load_incluster_config()
	return client.AppsV1Api()

def create_deployment(scheduler):
	global cli
	deployment_file = f'manifest/{scheduler}_deployment.yaml'
	file = open(deployment_file, 'r')
	deployment = yaml.safe_load(file)
	try:
		resp = cli.create_namespaced_deployment(body=deployment, namespace=NAMESPACE)
	except client.exceptions.ApiException as e:
		print("Exception : ", e)
		cli = create_client(ENVIRONMENT)
		resp = cli.create_namespaced_deployment(body=deployment, namespace=NAMESPACE)
	print(f"{datetime.now()} : Deployment created. Status='{resp.metadata.name}'")
	return deployment

def scale_deployment(deployment):
	global cli
	deployment['spec']['replicas'] += 1
	try:
		resp = cli.patch_namespaced_deployment(name=DEPLOYMENT_NAME, namespace=NAMESPACE, body=deployment)
	except client.exceptions.ApiException as e:
		print("Exception : ", e)
		cli = create_client(ENVIRONMENT)
		resp = cli.patch_namespaced_deployment(name=DEPLOYMENT_NAME, namespace=NAMESPACE, body=deployment)
	except Exception as e:
		print("Exception : ", e)
	print(f"{datetime.now()} : Deployment scaled. Status='{resp.metadata.name}'")
	return deployment

def delete_deployment():
	global cli
	try:
		resp = cli.delete_namespaced_deployment(name=DEPLOYMENT_NAME,namespace=NAMESPACE,body=client.V1DeleteOptions(propagation_policy="Foreground", grace_period_seconds=5))
	except client.exceptions.ApiException as e:
		print("Exception : ", e)
		cli = create_client(ENVIRONMENT)
		resp = cli.delete_namespaced_deployment(name=DEPLOYMENT_NAME,namespace=NAMESPACE,body=client.V1DeleteOptions(propagation_policy="Foreground", grace_period_seconds=5))
	print(f"{datetime.now()} : Deployment {DEPLOYMENT_NAME} deleted.")

cli = create_client(ENVIRONMENT)
print(f"{datetime.now()} : Client created")

## Peaks deployment
deployment = create_deployment("peaks")
time.sleep(SCALE_UP_DURATION)
for ins in range(MAX_INSTANCES):
	deployment = scale_deployment(deployment)
	time.sleep(SCALE_UP_DURATION)
## Deleting deployment
delete_deployment()
print(f"{datetime.now()} : Peaks Experiment completed")

time.sleep(SCALE_UP_DURATION)

## Default deployment
deployment = create_deployment("default")
time.sleep(SCALE_UP_DURATION)
for ins in range(MAX_INSTANCES):
	deployment = scale_deployment(deployment)
	time.sleep(SCALE_UP_DURATION)
## Deleting deployment
delete_deployment()
print(f"{datetime.now()} : Default Experiment completed")