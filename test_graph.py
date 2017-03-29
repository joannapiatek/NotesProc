import sys
import cv2
from detect_lines import *
import Graphs.Models as gm
import Graphs.Helpers as gh
import igraph as igraph
import Constants.Colors as colors
# import scipy.ndimage as ndimage


img = cv2.imread('img/test1.png', 0)
imgSize = np.shape(img)

graph = nx.Graph()
# graph = igraph.Graph()

# graph.add_edge(0, 1, weight = 2)


end = imgSize[0]
endCol = imgSize[1]
# for row in range(0, end):

# vertices = []
# for row in range(0, end):
#     for col in range(0, endCol):
#         name = str(row) + '_' + str(col)
#         vertices.append(name)
#
# graph.add_vertices(vertices)

edges_for_graph = []
weights = []
row = 0
for row in range(0, end):
    for col in range(0, endCol):
        color = img[row][col]
        nbhs = gh.get_neighbours((row, col), img,  imgSize)
        edges = gh.get_edges(gm.Pixel(row, col, color), nbhs)
        for edge in edges:
            graph.add_edge(edge.start, edge.end, weight=edge.weight)
            # edges_for_graph.append((edge.start, edge.end))
            # weights.append(edge.weight)

# graph.add_edges(edges_for_graph)
# graph.es["weight"] = weights


x = graph.node.keys()
staffLines = []

for row in range(0, end):
    if colors.BLACK not in img[row]:
        continue

    startNode = str(row) + '_' + str(0)
    endNode = str(row) + '_' + str(end)
    # startNode = (row, 0)
    # endNode = (row, end)
    result = nx.bidirectional_dijkstra(graph, startNode, endNode)
    staffLines.append(result)


sys.exit(0)
