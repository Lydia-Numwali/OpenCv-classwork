import cv2
import numpy as np
import zxing  # ZXing library

# Initialize ZXing reader
reader = zxing.BarCodeReader()

# Path to your barcode image
image_path = "./images/maxicode-example.png"  # Change this to your actual file

# Decode the PDF417 barcode
decoded = reader.decode(image_path)

# Print decoded text (only actual content)
if decoded:
    print(decoded.parsed)  # This prints the actual barcode text
else:
    print("Failed to decode the barcode.")
