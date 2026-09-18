import os

def generate_report(analysis, output_dir):
    path = os.path.join(output_dir, "report.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("SMART VISION - IMAGE ANALYSIS REPORT\n")
        f.write("=" * 45 + "\n")
        f.write(f"Image dimensions: {analysis['width']} x {analysis['height']}\n")
        f.write(f"Channels: {analysis['channels']}\n")
        f.write(f"Faces detected: {analysis['faces']}\n")
        f.write(f"Objects detected: {analysis['objects']}\n\n")
        f.write("Detected objects:\n")
        for item in analysis["detections"]:
            f.write(f"- {item['label']}: {item['confidence']:.2f}\n")
    return path
