import tensorflow as tf
import tf2onnx
from ultralytics import YOLO

# Convert YOLOv7-tiny model to TFLite
# Load the ONNX model
onnx_model_path = 'yolov7-tiny.onnx'
saved_model_dir = 'saved_model'

# Convert ONNX to TensorFlow SavedModel
tf2onnx.convert(opset=13, saved_model=saved_model_dir, output=onnx_model_path)

# Convert TensorFlow SavedModel to TFLite
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Save the TFLite model
with open('yolov7-tiny.tflite', 'wb') as f:
    f.write(tflite_model)

# Convert YOLOv8 model to TFLite
# Load the YOLOv8 model
model = YOLO('yolov8.pt')

# Export the model to TFLite format
model.export(format='tflite')