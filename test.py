import numpy as np
import cv2
import sys
from itertools import *
# from matplotlib import pyplot as plt


def encode(x):
    return [(name, len(list(group))) for name, group in groupby(x)]


img = cv2.imread('img/test.png', 0)
img = zip(*img)
imgSize = np.shape(img)

encoded = [imgSize[0]]
i = 0

for line in img:
    x = encode(img[i])
    encoded.append(x)
    i += 1

sys.exit(0)


