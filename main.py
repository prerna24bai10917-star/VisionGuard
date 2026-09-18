import argparse
import os
from modules.preprocessing import preprocess_image
from modules.face_detection import detect_faces
from modules.object_detection import detect_objects
from modules.image_analysis import analyze_image
from modules.report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="Smart Vision Computer Vision System")
    parser.add_argument("image", help="Path to the input image")
    parser.add_argument("--output", default="output", help="Output directory")
    args = parser.parse_args()

    if not os.path.isfile(args.image):
        raise FileNotFoundError(f"Input image not found: {args.image}")

    os.makedirs(args.output, exist_ok=True)
    image = preprocess_image(args.image, args.output)
    face_result = detect_faces(image)
    object_result = detect_objects(image, args.output)
    analysis = analyze_image(image, face_result, object_result)
    report_path = generate_report(analysis, args.output)

    print("\nSMART VISION ANALYSIS COMPLETE")
    print(f"Faces detected: {analysis['faces']}")
    print(f"Objects detected: {analysis['objects']}")
    print(f"Image size: {analysis['width']} x {analysis['height']}")
    print(f"Processed image: {object_result['output_path']}")
    print(f"Report: {report_path}")

if __name__ == "__main__":
    main()
