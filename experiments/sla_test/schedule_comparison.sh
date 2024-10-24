#!/bin/bash

# Configuration
Green="\033[0;32m"
ENDCOLOR="\e[0m"
NAMESPACE="default"           # Replace with your target namespace
POD_NAME_PREFIX="test-pod"    # Prefix for pod names
NUM_PODS=10                   # Maximum number of replicas to scale to
SCHEDULER_NAME="peaks"        # Use "peaks" for Peaks scheduler or comment for default
POD_IMAGE="nginx"             # Image to use for testing
SCHEDULER_FLAG=""             # Scheduler flag for deployment

DEPLOYMENT_NAME="default-stress-ng" # Name of the deployment
DEPLOYMENT_FILE="default_sng.yaml" # Path to your deployment configuration file


# Function to check if the deployment exists
check_deployment() {
    kubectl get deployment "$DEPLOYMENT_NAME" -n "$NAMESPACE" &> /dev/null
    return $?
}

# Function to get the current number of replicas
get_current_replicas() {
    kubectl get deployment "$DEPLOYMENT_NAME" -n "$NAMESPACE" -o jsonpath='{.spec.replicas}'
}

# FUnction to log time
log_scheduling_time(){
    START_TIME=$(date +%s%N)
    echo "$1"
    kubectl wait --for=condition=Ready pod/"$1" -n "$NAMESPACE" --timeout=60s
    END_TIME=$(date +%s%N)

    # Calculate scheduling time
    SCHEDULING_TIME=$((END_TIME - START_TIME))
    echo "$1: Scheduling Time (ns): $SCHEDULING_TIME" >> scheduling_times.log
}
# Function to deploy pods
deploy_pods() {
    local scheduler=$1
    # Use the scheduler name if provided, otherwise default scheduler
    if [ -z "$scheduler" ]; then
        DEPLOYMENT_FILE="./default_sng.yaml"
        DEPLOYMENT_NAME="default-stress-ng" 
    else
        DEPLOYMENT_FILE="./peaks_sng.yaml"
        DEPLOYMENT_NAME="peaks-stress-ng" 
    fi
    while true; do
        # Check if the deployment exists
        if ! check_deployment; then
            echo "Deployment '$DEPLOYMENT_NAME' does not exist. Applying the deployment..."
            kubectl apply -f "$DEPLOYMENT_FILE" -n "$NAMESPACE"

        else
            echo "Deployment '$DEPLOYMENT_NAME' exists. Checking current replicas..."
            CURRENT_REPLICAS=$(get_current_replicas)

            if [ "$CURRENT_REPLICAS" -lt "$NUM_PODS" ]; then
                NEW_REPLICAS=$((CURRENT_REPLICAS + 1))
                echo "Scaling deployment '$DEPLOYMENT_NAME' from $CURRENT_REPLICAS to $NEW_REPLICAS replicas..."
                kubectl scale deployment "$DEPLOYMENT_NAME" --replicas="$NEW_REPLICAS" -n "$NAMESPACE"

            else
                echo -e "${GREEN}Deployment '$DEPLOYMENT_NAME' is already scaled to the maximum of $NUM_PODS replicas.${ENDCOLOR}"
                break
            fi
        fi
        LAST_POD=$(kubectl get pods -n "$NAMESPACE" --selector=app="stress-ng" --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[-1].metadata.name}')
        echo "Last pod scheduled was $LAST_POD"
        log_scheduling_time $LAST_POD
    done    
}

# Deploy pods with the default scheduler
echo "Deploying pods with the default scheduler..."
deploy_pods ""

# Clean up pods
echo -e "${GREEN}Cleaning up pods...${ENDCOLOR}"
kubectl delete pod -l app=test-pod -n "$NAMESPACE" --force --grace-period=0

sleep 60

# Deploy pods with Peaks scheduler
echo "Deploying pods with Peaks scheduler..."
deploy_pods "$SCHEDULER_NAME"

# Calculate average and standard deviation
echo "Calculating average and standard deviation..."
awk '{sum += $NF; sumsq += ($NF)^2} END { 
    avg = sum / NR; 
    stddev = sqrt((sumsq / NR) - (avg^2)); 
    print "Average Scheduling Time (ns): " avg; 
    print "Standard Deviation (ns): " stddev; 
}' scheduling_times.log

# Clean up pods
echo "Cleaning up pods..."
kubectl delete pod -l app=test-pod -n "$NAMESPACE" --force --grace-period=0

echo "Scheduling time comparison complete!"


