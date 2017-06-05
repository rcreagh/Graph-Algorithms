#! usr/bin/python
"""This script is a Python implementation of Kruskal's greedy algorithm to find
the minimum spanning tree of a weighted, connected graph. If the graph is
unweighted, it considers all edges to have the same weight. 

This is not an efficient way to find the minimum spanning tree of a graph and
is for learning purposes only. This implementation is for use with Python's
Networkx graph library.

NOTE: This is WIP."""

import networkx
import union_find

class KruskalDisconnectedGraphException(Exception):
    """An exception raised if disconnected graph is passed."""
    pass

def kruskal(graph, return_networkx_graph=False):
    """Find the minimal spanning tree of a weighted, connected graph.
    
    Args:
        graph: Weighted graph in edge list representation.
        return_networkx_graph: Set output to be a networkx graph object.
    Returns:
        Either a list of weighted edges making up the minimal spanning tree of
        the graph, or a networkx graph of these weighted edges.
    """
    if not networkx.is_connected(graph):
        raise KruskalDisconnectedGraphException(
                "Graph passed in is not connected.")
    minimal_spanning_tree = []
    edges = graph.edges(data=True)
    try:
        sorted_edges = sorted(edges, key=lambda x: x[2])
    except:
        sorted_edges = edges
    total_nodes = graph.size()
    current_tree_size = 0
    ufs = union_find.UnionFind()
    for i, j, w in sorted_edges:
        if ufs.find(i) != ufs.find(j):
            minimal_spanning_tree.append((i, j, w))
            ufs.union(i, j)
            current_tree_size += 1
            # When minimal_spanning_tree has grown to n-1 edges, stop.
            if current_tree_size == total_nodes - 1:
                if return_networkx_graph:
                    return networkx.Graph(minimal_spanning_tree)
                else:
                    return minimal_spanning_tree
