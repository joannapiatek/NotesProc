import Graphs.Models as gm
import Constants.Colors as colors


def get_neighbours((x, y), array, array_size):
    d = 1
    x_left = x - d if x != 0 else 0
    x_right = x + d + 1 if x != array_size[0]-1 else x
    y_left = y - d if y != 0 else 0
    y_right = y + d + 1 if y != array_size[1]-1 else y
    neibs = []

    for i in range(x_left, x_right):
        for j in range(y_left, y_right):
            if x == i and y == j:
                continue
            neibs.append(gm.Pixel(i, j, array[i][j]))

    return neibs


def get_edges(center_pixel, neibs):
    edges = []

    for neib in neibs:
        weight = get_edge_weight(center_pixel, neib)
        edge = gm.GraphEdge((center_pixel.x_coor, center_pixel.y_coor), (neib.x_coor, neib.y_coor), weight)
        edges.append(edge)
    return edges


def get_edge_weight(start_pixel, end_pixel):
    if start_pixel.value == colors.BLACK or end_pixel.value == colors.BLACK:
        importance = 20
    else:
        importance = 60

    if start_pixel.x_coor == end_pixel.x_coor or start_pixel.y_coor == end_pixel.y_coor:
        return importance*10
    else:
        return importance*14
