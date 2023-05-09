import cv2
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Select the input image file
Tk().withdraw()
img_path = askopenfilename()

# Read the input image
img = cv2.imread(img_path)

# Apply Canny
edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)

# Select the output file name and location
output_path = asksaveasfilename(defaultextension='.png', filetypes=[('PNG', '*.png')])

# Save the result to a file
plt.imsave(output_path, edges, cmap='gray', format='png')

# Display the result
plt.figure()
plt.title('Edges')
plt.imshow(edges, cmap='gray')
plt.show()
