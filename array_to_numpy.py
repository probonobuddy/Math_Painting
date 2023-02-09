import numpy as np
from PIL import Image

# Create a 3D numpy array of 0s, then replace with numbers for colors
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

# Make a red patch
data[1:3, 0:2] = [255, 0, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')