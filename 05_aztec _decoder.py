import cv2
import pyzbar.pyzbar as pyzbar

# Load the image
image = cv2.imread("Image_05.png")

# Check if the image is loaded correctly
if image is None:
    print("Error: Unable to load the image.")
    exit(1)

# Decode the Aztec code
decoded = pyzbar.decode(image)

# Check if any Aztec code was found
if len(decoded) == 0:
    print("No Aztec code found in the image.")
else:
    # Extract the data from the decoded code
    data = decoded[0].data.decode("utf-8")
    print("Decoded data:", data)