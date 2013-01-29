import sys

class Node(object):
    def __init__(self, label):
        self.label = label
        self.distance = sys.maxint
        self.adjacent = None
        self.visited = False
        self.previous = None

    def __str__(self):
        return 'label: %s, d: %s' % (self.label, self.distance)

    def __repr__(self):
        return '%s' % (self.label)

def vertex_with_min_distance(vertices):
    min_vertex, min_distance = 0, sys.maxint

    for v in vertices:
        if v.distance < min_distance:
           min_vertex, min_distance = v, v.distance

    return min_vertex

def djikstra(source, dest, all):
    source.distance = 0

    current = source

    unvisited = all[:]
    unvisited.remove(current)

    while unvisited:
        for adjacent, distance in current.adjacent:
            if adjacent in unvisited and \
               current.distance + distance < adjacent.distance:
                adjacent.distance = current.distance + distance
                adjacent.previous = current

        current = vertex_with_min_distance(unvisited)
        unvisited.remove(current)

    path = []
    p = dest
    while p:
        path.insert(0, p)
        p = p.previous

    return path

if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.adjacent = [(b, 5), (c, 2)]
    b.adjacent = [(c, 1), (d, 4)]
    c.adjacent = [(d, 10)]

    path = djikstra(a, d, [a, b, c, d])

    print path
