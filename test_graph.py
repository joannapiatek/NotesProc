import sys
import cv2
from detect_lines import *
from networkx.readwrite import json_graph
import Constants.Colors as Colors
import json


# myFile = open('xdxdxd.txt', 'w')
# json.dump(xdxdxd, myFile)
# myFile.close()
# with open('data.json', 'w') as f:
#     json.dump(data, f)

img = cv2.imread('img/test1.png', 0)

graph = create_graph(img)
staffLines = detect_stafflines(graph, img)

with open('staffLines.json', 'w') as f:
    json.dump(staffLines, f)

sys.exit(0)
