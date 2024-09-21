import torch
import cv2
from flask import Flask, Response
from flask_cors import cross_origin

app = Flask(__name__)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class_names = model.names

def generate_frames():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            success, frame = camera.read()
            if not success:
                break

            # Resize frame for faster processing
            frame_resized = cv2.resize(frame, (640, 480))

            # Perform object detection
            results = model(frame_resized)

            # Draw bounding boxes and labels on the frame
            for result in results.xyxy[0]:
                x1, y1, x2, y2, conf, cls = result
                label = class_names[int(cls)]
                cv2.rectangle(frame_resized, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame_resized, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame_resized)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    finally:
        camera.release()

@app.route('/video_feed')
@cross_origin()
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
