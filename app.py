from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import numpy as np
import cv2
import base64   # ← required

app = Flask(__name__)
CORS(app)

# Load YOLO model (make sure yolov8n.pt is in your folder or in cache)
model = YOLO('yolov8n.pt')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        data = request.json['image']
        img_data = base64.b64decode(data.split(',')[1])
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Run detection with smaller size and lower conf threshold
        results = model(img, imgsz=320, conf=0.1)

        detections = []
        for r in results:
            for box in r.boxes:
                b = box.xyxy[0].cpu().numpy().tolist()  # [x1, y1, x2, y2]
                c = int(box.cls[0])
                conf = float(box.conf[0])
                detections.append({
                    'box': b,
                    'class': r.names[c],
                    'confidence': conf
                })

        return jsonify({'detections': detections})
    except Exception as e:
        print('Error in /detect:', e)
        return jsonify({'detections': []})

if __name__ == '__main__':
    app.run(port=5001, debug=True)

