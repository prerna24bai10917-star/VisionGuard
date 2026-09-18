# Smart Vision — Project Report

## 1. Cover Page
**Project:** Smart Vision — Image Analysis & Object Detection System  
**Domain:** Computer Vision  
**Student:** Prerna Bajpai  
**Institution:** VIT Bhopal University  
**Submission:** Flipped Course Evaluation — Build Your Own Project

## 2. Introduction
Computer Vision enables computers to extract useful information from digital images. This project implements a modular image-analysis pipeline that combines classical OpenCV preprocessing and face detection with pretrained deep-learning object detection.

## 3. Problem Statement
Manual inspection of images can be repetitive. The proposed system automates basic preprocessing, face detection, object detection, image statistics, and result reporting through a command-line workflow.

## 4. Functional Requirements
1. Validate and load an input image.
2. Perform grayscale, blur, and edge preprocessing.
3. Detect human faces.
4. Detect common objects using YOLO.
5. Count detections and extract image metadata.
6. Save processed outputs.
7. Generate a text report.
8. Execute entirely through the command line.

## 5. Non-Functional Requirements
- **Performance:** Use a lightweight YOLO model suitable for a student prototype.
- **Usability:** Provide a single command-line entry point.
- **Reliability:** Validate missing and unreadable input files.
- **Maintainability:** Separate processing, detection, analysis, and reporting into modules.
- **Resource Efficiency:** Use YOLOv8 Nano rather than a larger model.
- **Error Handling:** Raise clear errors for missing files and invalid images.

## 6. System Architecture
Input Image → Validation → Preprocessing → Face Detection + Object Detection → Analysis → Output and Report.

## 7. Design Diagrams
Insert the architecture, workflow, use-case, sequence, and component/class diagrams supplied with the project.

## 8. Design Decisions & Rationale
OpenCV was selected for image manipulation and classical computer-vision operations. Haar Cascade was selected for lightweight face detection. YOLOv8 Nano was selected as a pretrained object detector because it provides a practical balance between detection capability and computational cost for an academic prototype. The modular design separates concerns and simplifies testing.

## 9. Implementation Details
`main.py` coordinates the workflow. `preprocessing.py` performs grayscale, Gaussian blur, and Canny edge extraction. `face_detection.py` performs face detection. `object_detection.py` loads YOLO and creates annotated output. `image_analysis.py` computes image and detection statistics. `report_generator.py` creates the final text report.

## 10. Dataset / Model Description
This project does not train a new model. It uses a pretrained YOLOv8 Nano model supplied through Ultralytics. User-provided test images are used as inference inputs. The face detector uses OpenCV's pretrained Haar Cascade.

## 11. Evaluation Methodology
Evaluation is performed using:
- Successful image loading
- Correct creation of grayscale and edge outputs
- Number of detected faces
- Number and labels of detected objects
- Successful generation of an annotated image
- Successful generation of the text report
- Automated preprocessing validation tests

## 12. Results
Insert screenshots showing terminal execution, `processed.jpg`, `grayscale.jpg`, `edges.jpg`, and `report.txt`.

## 13. Testing Approach
Unit tests validate invalid input handling and creation of preprocessing outputs. End-to-end testing is performed by running the main command on a sample image and verifying all expected output files.

## 14. Challenges Faced
Potential challenges include model download time, computational limitations, variations in image quality, and detection errors caused by occlusion or unusual viewpoints.

## 15. Learnings & Key Takeaways
The project demonstrates how classical image processing can be combined with pretrained deep-learning models in a modular Computer Vision pipeline. It also demonstrates command-line execution, validation, testing, and structured software organization.

## 16. Future Enhancements
The system can be extended to webcam detection, JSON/CSV reporting, configurable confidence thresholds, model benchmarking, GPU acceleration, and a graphical or web interface.

## 17. References
- OpenCV Documentation
- Ultralytics YOLO Documentation
- Python Documentation
