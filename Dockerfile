# Use the official TensorFlow image as a base
FROM tensorflow/tensorflow:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the combined conversion script into the container
COPY convet_yolov_model_tflite.py /app/convet_yolov_model_tflite.py

# Set the working directory
WORKDIR /app

# Run the combined conversion script
CMD ["python3", "convet_yolov_model_tflite.py"]