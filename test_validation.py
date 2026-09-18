import os
import tempfile
import unittest
import numpy as np
import cv2
from modules.preprocessing import preprocess_image

class TestPreprocessing(unittest.TestCase):
    def test_invalid_image(self):
        with self.assertRaises(ValueError):
            preprocess_image("missing_image.jpg", "output")

    def test_preprocessing(self):
        with tempfile.TemporaryDirectory() as folder:
            image = np.zeros((100, 100, 3), dtype=np.uint8)
            path = os.path.join(folder, "test.jpg")
            cv2.imwrite(path, image)
            preprocess_image(path, folder)
            self.assertTrue(os.path.exists(os.path.join(folder, "grayscale.jpg")))
            self.assertTrue(os.path.exists(os.path.join(folder, "edges.jpg")))

if __name__ == "__main__":
    unittest.main()
