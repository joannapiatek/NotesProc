import numpy as np
import cv2
import sys
from itertools import *
from collections import Counter
from detect_lines import *

# import Models.PixelAfterRle as PixelAfterRle
# from matplotlib import pyplot as plt


img = cv2.imread('img/test.png', 0)
img = zip(*img)

encodedLines = get_color_sets_lengths(img)
(staffLineHeight, staffSpaceHeight) = calc_staff_heights(encodedLines)


sys.exit(0)


