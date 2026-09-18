```mermaid
flowchart TD
A[Input Image] --> B[Input Validation]
B --> C[Image Preprocessing]
C --> D[Face Detection]
C --> E[YOLO Object Detection]
D --> F[Image Analysis]
E --> F
F --> G[Processed Image]
F --> H[Analysis Report]
```