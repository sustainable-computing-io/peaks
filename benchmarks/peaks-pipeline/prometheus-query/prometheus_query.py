import os
import requests
import pandas as pd
import time

# Get configuration from environment variables
PROMETHEUS_URL = os.getenv('PROMETHEUS_URL')
CSV_DIRECTORY = os.getenv('CSV_DIRECTORY', '/mnt/pvc/')
START_TIME = os.getenv('START_TIME')
END_TIME = os.getenv('END_TIME')
QUERY_INTERVAL = int(os.getenv('QUERY_INTERVAL', 60))  # Default to 60 seconds
# DEBUG_INTERVAL = int(os.getenv('DEBUG_INTERVAL', 100))

# Read the metrics list from environment variable (comma-separated)
METRICS_LIST = os.getenv('METRICS_LIST').split(',')

# Function to query Prometheus with a time range
def query_prometheus(query, start_time, end_time):
    try:
        params = {
            'query': query,
            'start': start_time,
            'end': end_time,
            'step': '60s'  # Adjust step size as needed
        }
        response = requests.get(PROMETHEUS_URL, params=params)
        response.raise_for_status()
        return response.json()['data']['result']
    except Exception as e:
        print(f"Error querying Prometheus: {e}")
        return []

# Function to save the results to a CSV file
def save_to_csv(data, filename):
    df = pd.DataFrame(data, columns=["instance", "timestamp", "value","mode"])
    csv_file_path = os.path.join(CSV_DIRECTORY, filename)
    df.to_csv(csv_file_path, index=False)
    print(f"Data saved to {csv_file_path}")

# Main function to query Prometheus for multiple metrics
def main():
    for metric in METRICS_LIST:
        metric_name = metric.replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace(',', '_')
        print(f"Querying metric: {metric}")
        
        # Query Prometheus for the current metric
        result = query_prometheus(metric, START_TIME, END_TIME)

        print(result)
        
        # Check if the result contains data
        if result:
            # Flatten the metric labels and values for better CSV format
            data = []
            for item in result:
                metric_labels = item['metric']
                values = item['values']
                instance = metric_labels.get('instance', 'unknown')  # Get the "instance" label or set it to "unknown"
                mode = metric_labels.get('mode', 'unknown')  # Get the "instance" label or set it to "unknown"

                for value in values:
                    timestamp = value[0]
                    metric_value = value[1]

                    # Append the instance, timestamp, and value to the data list
                    data.append({
                        "instance": instance,
                        "timestamp": timestamp,
                        "mode": mode,
                        "value": metric_value
                    })
            
            # Save the result to a CSV file named after the metric
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{metric_name}_data_{timestamp}.csv"
            save_to_csv(data, filename)
        else:
            print(f"No data found for the metric: {metric}")
        
        # Wait for the query interval before the next query
        time.sleep(QUERY_INTERVAL)

if __name__ == "__main__":
    main()
