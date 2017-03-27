class GraphEdge:
    def __init__(self, (start_x, start_y), (end_x, end_y), weight):
        self.start = str(start_x) + '_' + str(start_y)
        self.end = str(end_x) + '_' + str(end_y)
        self.weight = weight


class Pixel:
    def __init__(self, x_coor, y_coor, value):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.value = value

