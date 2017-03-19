import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('oko.jpg',0)

##cv2.namedWindow('image', cv2.WINDOW_NORMAL)
##cv2.waitKey(0)
##cv2.imshow('image',img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
