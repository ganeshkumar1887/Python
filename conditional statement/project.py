import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("C:\Users\91778\OneDrive\Desktop\python\conditionSta")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.show()  
# Display the grayscale image

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (11, 11), 0)
plt.imshow(blur, cmap='gray')
plt.show()  # Display the blurred image
