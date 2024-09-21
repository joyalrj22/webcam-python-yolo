import cv2


def generate_frames(model, class_names):
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
