# A connected path approach http://www.inescporto.pt/~arebelo/publications/2008JaimeICIP.pdf
# http://www.inescporto.pt/~jsc/publications/conferences/2007anaRebeloAXMEDIS.pdf

import numpy as np
from itertools import *
from collections import Counter
import networkx as nx


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


def get_shortest_path(graph, source, target):
    return nx.dijkstra_path(graph, source, target)


def from_biadjacency_matrix(A, create_using=None):
    import numpy as np
    kind_to_python_type = {'f': float,
                           'i': int,
                           'u': int,
                           'b': bool,
                           'c': complex,
                           'S': str,
                           'V': 'void'}
    try:  # Python 3.x
        blurb = chr(1245)  # just to trigger the exception
        kind_to_python_type['U'] = str
    except ValueError:  # Python 2.6+
        kind_to_python_type['U'] = unicode
    G = _prep_create_using(create_using)
    n, m = A.shape
    dt = A.dtype
    try:
        python_type = kind_to_python_type[dt.kind]
    except:
        raise TypeError("Unknown numpy data type: %s" % dt)

    # make sure we get isolated nodes
    G.add_nodes_from(range(n), part=0)
    G.add_nodes_from(range(n, n + m), part=1)

    # get a list of edges
    x, y = np.asarray(A).nonzero()

    # handle numpy constructed data type
    if python_type is 'void':
        fields = sorted([(offset, dtype, name) for name, (dtype, offset) in
                         A.dtype.fields.items()])
        for (u, v) in zip(x, y):
            attr = {}
            for (offset, dtype, name), val in zip(fields, A[u, v]):
                attr[name] = kind_to_python_type[dtype.kind](val)
            G.add_edge(u, n + v, attr)
    else:  # basic data type
        G.add_edges_from(((u, n + v, {'weight': python_type(A[u, v])})
                          for (u, v) in zip(x, y)))
    return G
