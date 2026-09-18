import os
import cv2

def detect_objects(image, output_dir):
    try:
        from ultralytics import YOLO
    except ImportError:
        raise ImportError("Install dependencies using: pip install -r requirements.txt")

    model = YOLO("yolov8n.pt")
    results = model(image, verbose=False)
    result = results[0]
    annotated = result.plot()
    output_path = os.path.join(output_dir, "processed.jpg")
    cv2.imwrite(output_path, annotated)

    detections = []
    if result.boxes is not None:
        names = result.names
        for cls, conf in zip(result.boxes.cls.tolist(), result.boxes.conf.tolist()):
            label = names[int(cls)]
            detections.append({"label": label, "confidence": float(conf)})
    return {"detections": detections, "output_path": output_path}
