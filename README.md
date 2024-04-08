# Road object detection

This project aims to detect various objects on the road using the YOLOv3 (You Only Look Once) algorithm implemented with OpenCV. The YOLO algorithm is a state-of-the-art, real-time object detection system that is fast and accurate.

## Features

1. Object Detection: Detects various objects present on the road such as cars, pedestrians, bicycles, and more.
2. Real-time Processing: Utilizes the YOLOv3 algorithm for real-time processing, making it suitable for applications requiring fast response times.
3. Customizable Thresholds: Allows customization of confidence and non-maximum suppression thresholds for fine-tuning detection accuracy.
4. Easy Integration: Simple integration into existing projects or systems due to the use of OpenCV, a popular computer vision library.

## Dependencies

1. OpenCV: The computer vision library used for image processing and object detection.
2. NumPy: Required for array manipulation and mathematical operations.

## Setup
1. Fork and Clone the repo.
2. Add the file downloaded from the link https://pjreddie.com/media/files/yolov3.weights to the directory.
3. Install the pakages like numpy, cv2, flask, etc.
4. Run the app.py file. The app starts running on the localhost.
5. Upload the image and it will show the processed image.

## backend
The model.py file contains the DL model to process the image.
The frontend is just the proof of concept could be developed in a better way if the time permits.

The screenshot of the frontend is:
![frontend](https://github.com/vikasgrewal16/Road-Object-Detection-using-YOLOv3/blob/main/frontend.jpg)

##About Model