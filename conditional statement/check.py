import cv2
image = cv2.imread('C:/Users/91778/Desktop/python/conditionSta/coins.jpg')
if image is None:
    print("Error: Image not loaded.")
else:
    print("Image loaded successfully.")
