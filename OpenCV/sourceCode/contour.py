import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Hide tkinter GUI window
Tk().withdraw()

# Ask user to select input file
input_file = askopenfilename(title="Select input image file", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
if not input_file:
    exit()

# Load the image
image = cv2.imread(input_file)
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(edged,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Ask user to select output file and location
output_file = asksaveasfilename(title="Save output image file", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")], defaultextension=".png")
if not output_file:
    exit()

# Save output image
cv2.imwrite(output_file, image)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
