#! usr/bin/python
"""This script is a Python implementation of Kruskal's greedy algorithm to find
the minimum spanning tree of a weighted, connected graph. This is not an efficient way to find the minimum spanning tree of a graph and is for learning
purposes only. This implementation is for use with Python's Networkx graph
library.

NOTE: This is WIP."""

import networkx
import union_find

def kruskal(graph):
    """Find the minimal spanning tree of a weighted, connected graph.
    
    Args:
        graph: Weighted graph in edge list representation.
    Returns:
        List of weighted edges making up the minimal spanning tree of the graph.
    """
    #TODO: Raise exception if data type is not networkx graph.
    #TODO: Add exception if graph is not connected.
    if not networkx.is_connected(graph):
        raise pass
    minimal_spanning_tree = []
    edges = graph.edges(data=True)
    #TODO: Add exception if unweighted graph passed in.
    try:
        sorted_edges = sorted(edges, key=lambda x: x[2])
    except:
        pass
    total_nodes = graph.size()
    current_tree_size = 0
    ufs = union_find.UnionFind()
    for i, j, w in sorted_edges:
        if ufs.find(i) != ufs.find(j):
            minimal_spanning_tree.append([(i, j, w)])
            ufs.union(i, j)
            current_tree_size += 1
            if current_tree_size == total_nodes - 1:
                return minimal_spanning_tree
