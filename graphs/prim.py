from random import choice

class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.adjacent = []

    def __repr__(self):
        return self.label

def connects(edge, mst):
    source, dest, _ = edge

    for s, d, _ in mst:
        if source == s or source == d or \
           dest == s or dest == d:
            return True

    return False

def min_connecting_edge(mst, edges):
    min_edge = None
    for edge in edges:
        if connects(edge, mst) \
           and (not min_edge or edge[2] < min_edge[2]):
            min_edge = edge
    return min_edge

def prim_mst(vertexes):
    mst = []

    edges = []
    for v in vertexes:
        for adjacent in v.adjacent:
            edges.append((v, adjacent[0], adjacent[1]))

    if not edges:
        return mst

    mst = [edges.pop()]

    while len(mst) < len(vertexes) - 1:
        min_edge = min_connecting_edge(mst, edges)
        edges.remove(min_edge)
        mst.append(min_edge)

    return mst

if __name__ == '__main__':
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')

    a.adjacent = [(b, 1), (c, 3), (d, 2)]
    b.adjacent = [(e, 2)]
    c.adjacent = [(e, 3)]

    mst = prim_mst([a, b, c, d, e])

    print mst
