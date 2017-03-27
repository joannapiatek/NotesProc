import cv2
import sys
from detect_lines import *

# import Models.PixelAfterRle as PixelAfterRle
# from matplotlib import pyplot as plt


img = cv2.imread('img/test.png', 0)
imgTransposed = zip(*img)

encodedLines = get_color_sets_lengths(imgTransposed)
(staffLineHeight, staffSpaceHeight) = calc_staff_heights(encodedLines)


imgHeight = np.shape(img)[0]
imgWidth = np.shape(img)[1]
graph = create_graph(img)

staffLines = []
BLACK_PERC = 0.75;
BLACK_RUN = staffSpaceHeight;
STRIP_HEIGHT = staffSpaceHeight;

loopCounter = 0
for row in img:
    if 0 not in row:
        loopCounter += 1
        continue
    start = (0, loopCounter)
    end = (imgWidth-1, loopCounter)
    path = get_shortest_path(graph, start, end)
    staffLines.append(path)
    loopCounter += 1

sys.exit(0)


