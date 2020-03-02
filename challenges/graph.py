import sys
from collections import deque, defaultdict

class Node(object):
    """Node of a undirected Graph ."""
    def __init__(self,value):
        self.value = value
        self.visited = False
        self.adjacent = set()

    """ Add node in undirected node """
    def add_node(self, ady_node):
        self.adjacent.add(ady_node)
        ady_node.adjacent.add(self)

    """ Return None if there is not more visited nodes """
    def get_next_no_visited(self):
        next_node = None
        for i in self.adjacent:
            if(not i.visited):
                i.visited = True
                next_node = i
                self.adjacent.remove(next_node)
                return next_node
    # Hash must be unique, and it is a inmutable
    def __hash__(self):
        return self.value

    def __eq__(self,other):
        return self.__hash__() == other.__hash__()


def BFS(dictn, root):
    queue = deque()
    breadth_count = 1
    root.visited = True
    queue.append(root)

    while(len(queue) > 0):
        next_node = queue.popleft()
        next_child_node = next_node.get_next_no_visited()
        while(next_child_node != None):
            dictn[next_child_node] = 0 if dictn[next_child_node] == -1 else dictn[next_child_node]
            dictn[next_node] = 0 if dictn[next_node] == -1 else dictn[next_node]
            dictn[next_child_node] = (dictn[next_node] + 6)
            queue.append(next_child_node)
            next_child_node = next_node.get_next_no_visited()
    return dictn

def get_node_from_set(this_set, node):
    for i in this_set:
        if(i == node):
            return i

def print_response(dictn, root):
    res = ""
    for k,v in BFS(dictn, root).iteritems():
        if k != root:
            res += "%s " % str(v)
    print(res)

####################################################################
num_test = int(input())
nodes = 0

for i in xrange(num_test):
    dictn = defaultdict(int)
    nodes,links = map(lambda x: int(x), raw_input().split())
    for i in xrange(nodes):
        dictn[Node(i+1)] = -1

    for i in xrange(links):
        n,c = map(lambda x: Node(int(x)), raw_input().split())
        n = get_node_from_set(dictn, n)
        c = get_node_from_set(dictn, c)
        n.add_node(c)
    root = get_node_from_set(dictn, Node(int(raw_input())))
    print_response(dictn, root)
