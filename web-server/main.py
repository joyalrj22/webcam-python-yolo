import torch
from flask import Flask, Response
from flask_cors import cross_origin
from frame_manipulation import generate_frames

app = Flask(__name__)


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
class_names = model.names


@app.route('/video_feed')
@cross_origin()
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
