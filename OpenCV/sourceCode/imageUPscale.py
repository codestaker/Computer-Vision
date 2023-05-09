import tkinter as tk
from tkinter import filedialog
from skimage import io, exposure

# Create the main window
root = tk.Tk()

# Set the window title and size
root.title('Image Processor')
root.geometry('500x500')

# Define the callback function for the brightness slider
def update_brightness(value):
    # Load the original image
    image = io.imread(image_path)
    # Adjust the brightness using scikit-image's exposure module
    adjusted_image = exposure.adjust_gamma(image, gamma=float(value) / 50)
    # Update the image preview
    image_preview.configure(image=tk.PhotoImage(adjusted_image))

# Define the callback function for the contrast slider
def update_contrast(value):
    # Load the original image
    image = io.imread(image_path)
    # Adjust the contrast using scikit-image's exposure module
    adjusted_image = exposure.adjust_sigmoid(image, gain=float(value) / 50, cutoff=0.5)
    # Update the image preview
    image_preview.configure(image=tk.PhotoImage(adjusted_image))

# Define the callback function for the "Save" button
def save_image():
    # Get the file path to save the processed image to
    save_path = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG', '*.png'), ('JPEG', '*.jpg'), ('All Files', '*.*')]
    )
    # Load the original image
    image = io.imread(image_path)
    # Adjust the brightness and contrast using scikit-image's exposure module
    brightness = brightness_slider.get()
    contrast = contrast_slider.get()
    adjusted_image = exposure.adjust_gamma(image, gamma=float(brightness) / 50)
    adjusted_image = exposure.adjust_sigmoid(adjusted_image, gain=float(contrast) / 50, cutoff=0.5)
    # Save the processed image to the specified location
    io.imsave(save_path, adjusted_image)

# Define the callback function for the "Open" button
def open_image():
    # Get the file path to the selected image
    global image_path
    image_path = filedialog.askopenfilename(
        filetypes=[('Images', '*.png;*.jpg;*.jpeg;*.bmp;*.gif'), ('All Files', '*.*')]
    )
    # Load the selected image and update the image preview
    image = io.imread(image_path)
    image_preview.configure(image=tk.PhotoImage(image))
    # Reset the brightness and contrast sliders
    brightness_slider.set(50)
    contrast_slider.set(50)

# Create the brightness slider
brightness_slider = tk.Scale(
    root, from_=0, to=100, orient=tk.HORIZONTAL,
    label='Brightness', command=update_brightness
)
brightness_slider.pack()

# Create the contrast slider
contrast_slider = tk.Scale(
    root, from_=0, to=100, orient=tk.HORIZONTAL,
    label='Contrast', command=update_contrast
)
contrast_slider.pack()

# Create the "Save" button
save_button = tk.Button(root, text='Save', command=save_image)
save_button.pack()

# Create the "Open" button
open_button = tk.Button(root, text='Open', command=open_image)
open_button.pack()

# Create the image preview widget
image_preview = tk.Label(root)
image_preview.pack()

# Start the main event loop
root.mainloop()
