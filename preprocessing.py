import cv2
import os

def preprocess_image(image_path, output_dir):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Unable to read the input image.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    cv2.imwrite(os.path.join(output_dir, "grayscale.jpg"), gray)
    cv2.imwrite(os.path.join(output_dir, "edges.jpg"), edges)
    return image
