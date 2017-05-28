#! usr/bin/python
"""This script is a Python implementation of Kruskal's greedy algorithm to find
the minimum spanning tree of a weighted, connected graph. This is not an efficient way to find the minimum spanning tree of a graph and is for learning
purposes only. This implementation is for use with Python's Networkx graph
library.

NOTE: This is WIP."""

import networkx

def kruskal(graph):
    minimal_spanning_tree = []
    edges = sorted(list(graph.edges()))
    total_nodes = graph.size()
    current_tree_size = 0
    for i in edges:
        #TODO: Implement union find and complete this.
        pass
