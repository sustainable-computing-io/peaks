# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and other necessary files
COPY training_script.py /app/

# Install required Python packages
RUN pip install pandas scikit-learn joblib

# Set environment variables for CSV file and model output paths
ENV CSV_PATH=/mnt/pvc/data/training_data.csv
ENV MODEL_OUTPUT_PATH=/mnt/pvc/model_output/model.pkl

# Run the training script
CMD ["python", "training_script.py"]
