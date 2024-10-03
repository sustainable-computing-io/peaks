import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Function to load and combine multiple CSV files from a directory
def load_data_from_directory(directory):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    dataframes = []
    metrics_file_map = {}
    
    # Load each CSV file and append to the list
    for csv_file in csv_files:
        file_path=""
        if "node_cpu_seconds" in csv_file:
            file_path = os.path.join(directory, csv_file)
            metrics_file_map.update({"cpu_util_file":file_path})
        elif "kepler_node_package_joules_total" in csv_file:
            file_path = os.path.join(directory, csv_file)
            metrics_file_map.update({"node_package_power":file_path})
        elif "kepler_node_dram_joules_total" in csv_file:
            file_path = os.path.join(directory, csv_file)
            metrics_file_map.update({"node_dram_power":file_path})
    
    print(f"Metric files{metrics_file_map}")

    node_package_power = pd.read_csv(metrics_file_map.get("node_package_power"))
    node_package_power = node_package_power.groupby(['instance', 'timestamp'], as_index=False)['value'].sum()
    node_package_power['timestamp'] = pd.to_datetime(node_package_power['timestamp'])

    node_dram_power = pd.read_csv(metrics_file_map.get("node_dram_power"))
    node_dram_power = node_dram_power.groupby(['instance', 'timestamp'], as_index=False)['value'].sum()
    node_dram_power['timestamp'] = pd.to_datetime(node_dram_power['timestamp'])

    node_power_metrics = pd.merge(node_package_power, node_dram_power, on = ["timestamp", "instance"])
    node_power_metrics = node_power_metrics.rename(columns={"value_x":"package", "value_y":"dram"})
    node_power_metrics['power'] = node_power_metrics['package'] + node_power_metrics['dram']

# Clean the data (e.g., handle missing values)
def clean_data(df):
    # Drop rows with missing values (customize this step as needed)
    df_cleaned = df.dropna()
    print(f"Data cleaned: {df_cleaned.shape[0]} rows remaining after cleaning")
    return df_cleaned

# Train a simple machine learning model (e.g., linear regression)
def train_model(df):
    # For this example, assume the 'value' column is the target, and 'timestamp' is the feature
    X = df[['timestamp']]  # Feature
    y = df['value']        # Target

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Print the model's performance
    print(f"Model trained. Coefficients: {model.coef_}, Intercept: {model.intercept_}")
    return model

# Save the model to a file
def save_model(model, output_path):
    joblib.dump(model, output_path)
    print(f"Model saved to {output_path}")

def main():
    # Get the CSV directory and model output path from environment variables
    csv_directory = os.getenv("CSV_PATH", "/mnt/pvc/data/")
    model_output_path = os.getenv("MODEL_OUTPUT_PATH", "/mnt/pvc/model_output/model.pkl")

    # Load, combine, and clean the data
    df = load_data_from_directory(csv_directory)
    df_cleaned = clean_data(df)

    # Train the model
    model = train_model(df_cleaned)

    # Save the trained model
    save_model(model, model_output_path)

if __name__ == "__main__":
    main()
