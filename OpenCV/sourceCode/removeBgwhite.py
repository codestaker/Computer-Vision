import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Initialize tkinter and hide root window
root = Tk()
root.withdraw()

# Ask user to select input image file
input_file = askopenfilename(title='Select Input Image', filetypes=[('Image Files', '*.jpg;*.jpeg;*.png;*.bmp')])

# Read input image
img = cv2.imread(input_file)

# Create a mask initialized with zeros for background and foreground segmentation
mask = np.zeros(img.shape[:2], np.uint8)

# Initialize background and foreground models using default values
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Define the region of interest (ROI) for GrabCut algorithm
rect = cv2.selectROI('Input Image', img, fromCenter=False, showCrosshair=True)

# Apply GrabCut algorithm to segment the foreground from the background
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Create a binary mask for the foreground using the segmented mask
mask_fg = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype('uint8')

# Apply the binary mask to the original image to extract the foreground
img_fg = cv2.bitwise_and(img, img, mask=mask_fg)

# Ask user to select output image file and save the extracted foreground image
output_file = asksaveasfilename(title='Save Output Image', defaultextension='.png', filetypes=[('PNG', '*.png')])
cv2.imwrite(output_file, img_fg)

# Show the extracted foreground image in full scale
cv2.namedWindow('Output Image', cv2.WINDOW_NORMAL)
cv2.imshow('Output Image', img_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
