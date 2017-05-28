#! usr/bin/python
"""This script uses breadth first search to find the shortest path from a 
specified root node to every other node in a component of an unweighted graph.
Uses Python's Networkx graphs. If a graph is weighted, simply returns the
component of the root node."""

import networkx

class Vertex(object):
    def __init__(self, name, parent_node, height):
        self.name = name
        self.parent_node = parent_node
        self.height = height

    def __repr__(self):
        node = str([self.name, self.parent_node, self.height])
        return node

def breadth_first_search(graph, node):
    """ Traverse a graph breadth first.

    Args:
        graph: Networkx graph. Must be unweighted.
        node: Root node we will traverse the graph from.
    Returns:
        Subgraph of graph that contains the shortest path from the root_node
        to every other node, the parent node for each node in the tree and the
        height of each node in the tree (ie. the distance from the root node).
    """
    sub_graph = []
    queue = set()
    root_node = Vertex(node, None, 0)
    sub_graph.append(root_node)
    queue.add(root_node)
    while queue:
        current_node = queue.pop()
        for neighbor in graph.neighbors(current_node.name):
            if neighbor not in [i.name for i in sub_graph]:
                neighboring_node = Vertex(
                        neighbor, current_node.name, current_node.height + 1)
                queue.add(neighboring_node)
                sub_graph.append(neighboring_node)
    return (sub_graph)
