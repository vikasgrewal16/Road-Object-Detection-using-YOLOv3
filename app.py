from flask import Flask, render_template, request, send_file
from model import perform_object_detection
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image_file = request.files['image']
    image_path = "static/uploaded_image.jpg"
    image_file.save(image_path)
    
    config_path = "D:/Shikhar/Road_object_detection/yolov3.cfg"
    weights_path = "D:/Shikhar/Road_object_detection/yolov3.weights"
    classes_path = "D:/Shikhar/Road_object_detection/yolov3.txt"
    
    perform_object_detection(image_path, config_path, weights_path, classes_path)
    result_image_path = "D:/Shikhar/Road_object_detection/object-detection.jpg"
    image = cv2.imread(result_image_path)

    return send_file(result_image_path, mimetype='image/jpg')

if __name__ == "__main__":
    app.run(debug=True)
