#!/bin/bash

# Read configuration values from environment variables (provided via ConfigMap)
MAX_CPU_LOAD=${MAX_CPU_LOAD:-100}  # Default to 100% if not provided
STEP=${STEP:-10}                   # Default to 10% increment if not provided
DURATION=${DURATION:-350}            # Default to 60 seconds if not provided
CPU_COUNT=$(nproc)                  # Number of CPU cores available

# Run the stress-ng workload in incremental steps
for i in $(seq $STEP $STEP $MAX_CPU_LOAD); do
  WORKERS=$(($i * $CPU_COUNT / 100))
  echo "Stressing CPU with $WORKERS workers for $DURATION seconds"
  stress-ng --cpu $WORKERS --timeout ${DURATION}s
  sleep 10
done

echo "CPU stress test completed."
