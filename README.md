# Smart Vision — Image Analysis & Object Detection System

## Overview
Smart Vision is a modular Computer Vision project implemented in Python. It combines OpenCV image preprocessing, Haar Cascade face detection, and pretrained YOLO object detection. The application runs from the command line and produces processed images and a text analysis report.

## Features
- Input validation
- Grayscale conversion
- Gaussian blur
- Canny edge detection
- Face detection
- YOLO object detection
- Object and face counting
- Output image generation
- Text report generation
- Automated validation tests

## Technologies
- Python 3
- OpenCV
- Ultralytics YOLO
- NumPy
- unittest

## Project Structure
```text
smart-vision/
├── main.py
├── requirements.txt
├── statement.md
├── README.md
├── modules/
│   ├── preprocessing.py
│   ├── face_detection.py
│   ├── object_detection.py
│   ├── image_analysis.py
│   └── report_generator.py
├── input/
├── output/
├── models/
├── tests/
├── diagrams/
└── report/
```

## Installation
Install Python 3.10 or newer, then open a terminal in the repository folder.

```bash
python -m pip install -r requirements.txt
```

The first YOLO execution may download the pretrained `yolov8n.pt` model automatically. Internet access is therefore required for the first object-detection run unless the model file is already present.

## Input
Place an image in the `input` folder, for example:

```text
input/sample.jpg
```

## Run
From the repository root:

```bash
python main.py input/sample.jpg
```

Or specify another output directory:

```bash
python main.py input/sample.jpg --output output
```

## Output
The program creates:
- `output/grayscale.jpg`
- `output/edges.jpg`
- `output/processed.jpg`
- `output/report.txt`

The terminal reports the number of detected faces and objects.

## Testing
Run:

```bash
python -m unittest discover -s tests -v
```

## Model
The project uses the pretrained YOLOv8 Nano model through Ultralytics. It is selected for a lightweight academic prototype because it provides object detection with relatively low computational requirements.

## Limitations
Detection quality depends on image quality, object size, lighting, viewpoint, and the pretrained model's learned classes. The system should not be used as a safety-critical decision system.

## Future Enhancements
- Webcam/live video mode
- Confidence threshold configuration
- More detection models
- CSV/JSON reports
- Web interface
- GPU acceleration
- Model comparison and performance benchmarking

## License
This project is intended for academic and educational use.
