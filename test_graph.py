import sys
import cv2
from detect_lines import *
import Graphs.Models as gm
import Graphs.Helpers as gh
import igraph as igraph
import Constants.Colors as colors
# import scipy.ndimage as ndimage


img = cv2.imread('img/test.png', 0)
imgSize = np.shape(img)

# graph = nx.Graph()
graph = igraph.Graph()
graph.add_vertex(10)
# graph.add_edge(0, 1, weight = 2)


end = imgSize[0]
endCol = imgSize[1]
# for row in range(0, end):

for row in range(0, end):
    for col in range(0, endCol):
        name = str(row) + '_' + str(col)
        graph.add_vertex(name)

row = 0
for row in range(0, end):
    for col in range(0, endCol):
        color = img[row][col]
        nbhs = gh.get_neighbours((row, col), img,  imgSize)
        edges = gh.get_edges(gm.Pixel(row, col, color), nbhs)
        for edge in edges:
            graph.add_edge(edge.start, edge.end, weight=edge.weight)


staffLines = []
xd = graph.node.keys()

for row in range(0, end):
    # if colors.BLACK not in img[row]:
    #     continue

    startNode = (row, 0)
    endNode = (row, end)
    result = nx.bidirectional_dijkstra(graph, startNode, endNode)
    staffLines.append(result)


sys.exit(0)
