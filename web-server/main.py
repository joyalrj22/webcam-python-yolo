from flask import Flask, Response, request, jsonify
from flask_cors import cross_origin
from frame_manipulation import generate_frames
from dtos.camera_filters import Filter, FilterType
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/video_feed')
@cross_origin()
def video_feed():
    filter_type = request.args.get('type')
    return Response(generate_frames(Filter(type=FilterType[filter_type])), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
