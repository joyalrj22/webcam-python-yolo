import cv2
import torch

from dtos.camera_filters import Filter, FilterType

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
class_names = model.names


def generate_frames(filter: Filter):
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        return

    try:
        while True:
            success, frame = camera.read()
            if not success:
                break

            frame_resized = cv2.resize(frame, (640, 480))

            object_classification(frame_resized, filter.type)

            ret, buffer = cv2.imencode('.jpg', frame_resized)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    finally:
        camera.release()


def run_yolo_model(frame):
    model_results = model(frame)
    for result in model_results.xyxy[0]:
        x1, y1, x2, y2, conf, cls = result
        yield x1, y1, x2, y2, conf, cls


def object_classification(frame, filter_type: FilterType):
    for x1, y1, x2, y2, conf, cls in run_yolo_model(frame):
        label = class_names[int(cls)]
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# def box_filter(frame)


