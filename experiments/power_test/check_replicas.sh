#!/bin/bash

# Define the deployment name and namespace
DEPLOYMENT_NAME="peaks-stress-ng" # Change this to your deployment name
NAMESPACE="kube-system"       # Change this if your deployment is in a different namespace

# Get the list of pods for the deployment
PODS=$(kubectl get pods -n $NAMESPACE -l app=$DEPLOYMENT_NAME -o jsonpath='{.items[*].metadata.name}')

# Print header for the table
printf "%-30s %-20s\n" "POD NAME" "NODE"
echo "----------------------------------------"

# Loop through each pod and get the node it's assigned to
for POD in $PODS; do
    NODE=$(kubectl get pod $POD -n $NAMESPACE -o jsonpath='{.spec.nodeName}')
    printf "%-30s %-20s\n" "$POD" "$NODE"
done
