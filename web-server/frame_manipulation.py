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

            match filter.type:
                case FilterType.OBJECT_DETECTION:
                    object_classification(frame_resized)
                case FilterType.BOX_FILTER:
                    apply_filter(lambda frame: cv2.blur(frame, (5, 5)), frame_resized)
                case FilterType.GAUSSIAN_FILTER:
                    apply_filter(lambda frame: cv2.GaussianBlur(frame, (5, 5), 0), frame_resized)
                case FilterType.MEDIAN_FILTER:
                    apply_filter(lambda frame: cv2.medianBlur(frame, 5), frame_resized)

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


def object_classification(frame):
    for x1, y1, x2, y2, conf, cls in run_yolo_model(frame):
        label = class_names[int(cls)]
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


def apply_filter(filter_fn, frame):
    for x1, y1, x2, y2, conf, cls in run_yolo_model(frame):
        if class_names[int(cls)] == 'person':
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            frame[y1:y2, x1:x2] = filter_fn(frame[y1:y2, x1:x2])