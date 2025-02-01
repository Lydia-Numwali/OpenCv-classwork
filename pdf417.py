import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Load the image
image_path = "./images/IMG_1903 2.jpg"  # Use your uploaded image path
image = cv2.imread(image_path)

# Convert to grayscale (optional but improves detection)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Decode barcodes
barcodes = decode(gray)

# Process detected barcodes
if barcodes:
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        print(f"Decoded Data: {barcode_data}")
        print(f"Barcode Type: {barcode_type}")
else:
    print("No PDF417 barcode found in the image.")
