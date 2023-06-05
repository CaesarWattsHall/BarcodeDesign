# This program generates a random 12-digit number using the random library. 
# It then uses the code128 library to generate a barcode image from this number. 
# The barcode image is saved as a PNG file using the save method. 
# Finally, the program prints a message indicating that the barcode has been saved.
#
# By: Caesar R. Watts-Hall
# Date: June 05, 2023

import code128
import random

# Generate a random 12-digit number
barcode_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])

# Generate the barcode image
barcode_image = code128.image(barcode_number)

# Save the barcode image
barcode_image.save("barcode.png")

print(f"Barcode saved as barcode.png")
