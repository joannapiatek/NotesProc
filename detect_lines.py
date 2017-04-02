# A connected path approach http://www.inescporto.pt/~arebelo/publications/2008JaimeICIP.pdf
# http://www.inescporto.pt/~jsc/publications/conferences/2007anaRebeloAXMEDIS.pdf

import numpy as np
from itertools import *
from collections import Counter
import networkx as nx
import Graphs.Helpers as gh
import Graphs.Models as gm
import Constants.Colors as Colors


def encode_rle(x):
    return [(name, len(list(group))) for name, group in groupby(x)]


def calc_staff_heights(lines):
    lines = sorted(lines)
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


# test performance if edges added as a list
def create_graph(img):
    img_size = np.shape(img)

    end = img_size[0]
    end_col = img_size[1]

    graph = nx.Graph()

    for row in range(0, end):
        for col in range(0, end_col):
            color = img[row][col]
            nbhs = gh.get_neighbours((row, col), img, img_size)
            edges = gh.get_edges(gm.Pixel(row, col, color), nbhs)
            for edge in edges:
                graph.add_edge(edge.start, edge.end, weight=edge.weight)

    return graph


def is_path_black_enough(path, img):

    black_pixels_count = 0

    for pixel in path:
        values = pixel.split("_")
        row = int(values[0])
        col = int(values[1])
        color = img[row][col]
        if color == Colors.BLACK:
            black_pixels_count += 1

    path_leng = np.shape(path)[0]
    compare = black_pixels_count/(path_leng * 1.0)
    if compare > 0.7:
        return True
    return False


def detect_stafflines(graph, img):
    staff_lines = []
    img_size = np.shape(img)
    end = img_size[0]

    for row in range(0, end):
        if Colors.BLACK not in img[row]:
            continue

        start_node = str(row) + '_' + str(0)
        end_node = str(row) + '_' + str(end)
        path = nx.bidirectional_dijkstra(graph, start_node, end_node)
        if is_path_black_enough(path[1], img):
            staff_lines.append(path)

    return staff_lines
