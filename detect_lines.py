# A connected path approach http://www.inescporto.pt/~arebelo/publications/2008JaimeICIP.pdf

import numpy as np
import cv2
import sys
from itertools import *
from collections import Counter


def encode_rle(x):
    return [(name, len(list(group))) for name, group in groupby(x)]


def calc_staff_heights(lines):
    lines = sorted(lines);
    counted_pairs = Counter(elem for elem in lines)
    most_common = counted_pairs.most_common(counted_pairs.__len__())

    line_height = next((x for x in most_common if x[0][0] == 0), None)[0][1]
    space_height = next((x for x in most_common if x[0][0] == 255), None)[0][1]
    return line_height, space_height


def get_color_sets_lengths(image):

    img_size = np.shape(image)
    encoded_lines = []

    for line in image:
        encoded_item = encode_rle(line)
        if encoded_item != [(255, img_size[1])] and encoded_item.__len__() % 10 == 1:
            encoded_lines += encoded_item
    return encoded_lines

