# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and any necessary files into the container
COPY prometheus_query.py /app/

# Install necessary Python libraries
RUN pip install requests pandas

# Set environment variables for configurable properties (these will be overridden by Kubernetes ConfigMap)
ENV PROMETHEUS_URL="http://localhost:9090/api/v1/query_range"
ENV METRICS_LIST='kepler_node_dram_joules_total,kepler_node_other_joules_total,kepler_node_package_joules_total,kepler_node_platform_joules_total,node_cpu_seconds_total'
ENV CSV_DIRECTORY="/tmp/pvc/data"
ENV QUERY_INTERVAL="60"
ENV START_TIME="2024-09-05T10:50:00Z"
ENV END_TIME="2024-09-05T11:56:00Z"

# Expose the working directory (in case files need to be written to the mounted PVC)
VOLUME ["/mnt/pvc"]

# Run the Python script to query Prometheus
CMD ["python", "prometheus_query.py"]
