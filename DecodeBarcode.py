# This code uses the decode function from the pyzbar library to decode the barcode in the image. 
# The decoded data is then printed to the console.
#
# By: Caesar R. Watts-Hall
# Date: June 05, 2023

from pyzbar.pyzbar import decode
from PIL import Image

# Load the image
image = Image.open("barcode.png")

# Decode the barcode
decoded_objects = decode(image)

# Print the decoded data
for obj in decoded_objects:
    print(f"Type: {obj.type}")
    print(f"Data: {obj.data.decode('utf-8')}")
