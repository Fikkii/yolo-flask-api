# YOLO Image Detection API (Flask + YOLOv8n)

This is a lightweight image detection backend built with [Flask](https://flask.palletsprojects.com/) and [YOLOv8n](https://github.com/ultralytics/ultralytics) (nano model). The API accepts images and returns detection results using the efficient `yolov8n.pt` model.

## Features

- Fast and lightweight image detection
- Simple REST API built with Flask
- Uses YOLOv8n (`yolov8n.pt`) for efficient inference

## Getting Started

### Prerequisites

- Python 3.8+
- All dependencies listed in `requirements.txt`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Fikkii/yolo-flask-api.git
   cd yolo-flask-api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app:**
   ```bash
   python app.py
   ```

## Frontend

The frontend for this project is available at:  
[https://github.com/Fikkii/yolo-detection](https://github.com/Fikkii/yolo-detection)

## Contributing

I'm open for collaborations!  
Feel free to fork, open issues, or contact me anytime.
