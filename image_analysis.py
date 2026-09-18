def analyze_image(image, faces, object_result):
    height, width = image.shape[:2]
    return {
        "width": width,
        "height": height,
        "channels": image.shape[2] if len(image.shape) == 3 else 1,
        "faces": len(faces),
        "objects": len(object_result["detections"]),
        "detections": object_result["detections"]
    }
