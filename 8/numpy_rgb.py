from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("input.jpg")  
img_np = np.array(img)  

red, _ = np.histogram(img_np[:,:,0], bins=256, range=(0,255))
green, _ = np.histogram(img_np[:,:,1], bins=256, range=(0,255))
blue, _ = np.histogram(img_np[:,:,2], bins=256, range=(0,255))

plt.figure(figsize=(10,5))
plt.plot(red, color='red', label='Red')
plt.plot(green, color='green', label='Green')
plt.plot(blue, color='blue', label='Blue')
plt.title("RGB Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()
