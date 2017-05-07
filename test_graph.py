import sys
import cv2
from detect_lines import *
import json

img = cv2.imread('img/test1.png', 0)
# staffLines = get_stafflines_from_img(img)

with open('staffLines.json') as data_file:
    rawStaffLines = json.load(data_file)

staffLines = []
# Create a black image
img_size = np.shape(img)
blank_img = np.zeros((img_size[0], img_size[1], 3), np.uint8)
blank_img.fill(100)

for rawLine in rawStaffLines:
    for pixel_string in rawLine[1]:
        pixel = create_pixel_from_pixel_string(pixel_string, img)
        #blank_img[pixel.x_coor][pixel.y_coor] = pixel.value
        #staffLines.append(pixel)
        if pixel.value == Colors.BLACK:
            img[pixel.x_coor, pixel.y_coor] = Colors.WHITE


# cv2.imwrite('img/test1_stafflines.png', blank_img)
cv2.imwrite('img/test1_no_stafflines.png', img)

sys.exit(0)
