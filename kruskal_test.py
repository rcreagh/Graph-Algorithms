#! /usr/bin/python
"""Unit tests for kruskal.py.

NOTE: This is WIP."""
import kruskal
import networkx
import unittest

class KruskalTest(unittest.TestCase):
    
    def testKruskalDisconnectedGraph(self):
        graph = networkx.Graph()
        graph.add_edge(0, 1, weight=0.6)
        graph.add_edge(1, 2, weight=0.2)
        graph.add_edge(1, 3, weight=0.1)
        graph.add_edge(2, 4, weight=0.7)
        graph.add_edge(5, 6, weight=0.9)
        graph.add_edge(0, 4, weight=0.3)

        self.assertRaises(kruskal.KruskalDisconnectedGraphException,
                kruskal.kruskal, graph)

    def testKruskalWeightedGraph(self):
        graph = networkx.Graph()
        graph.add_edge(0, 1, weight=0.6)
        graph.add_edge(1, 2, weight=0.2)
        graph.add_edge(1, 3, weight=0.1)
        graph.add_edge(2, 4, weight=0.7)
        graph.add_edge(2, 5, weight=0.9)
        graph.add_edge(2, 6, weight=0.3)
        graph.add_edge(6, 3, weight=1.1)

        expected = [
                (1, 3, {'weight': 0.1}), (1, 2, {'weight': 0.2}),
                (2, 6, {'weight': 0.3}), (0, 1, {'weight': 0.6}),
                (2, 4, {'weight': 0.7}), (2, 5, {'weight': 0.9})]

        self.assertEqual(expected, kruskal.kruskal(graph))

    def testKruskalWeightedGraphReturnNxGraph(self):
        graph = networkx.Graph()
        graph.add_edge(0, 1, weight=0.6)
        graph.add_edge(1, 2, weight=0.2)
        graph.add_edge(1, 3, weight=0.1)
        graph.add_edge(2, 4, weight=0.7)
        graph.add_edge(2, 5, weight=0.9)
        graph.add_edge(2, 6, weight=0.3)
        graph.add_edge(6, 3, weight=1.1)

        expected = [
                (1, 3, {'weight': 0.1}), (1, 2, {'weight': 0.2}),
                (2, 6, {'weight': 0.3}), (0, 1, {'weight': 0.6}),
                (2, 4, {'weight': 0.7}), (2, 5, {'weight': 0.9})]

        self.assertItemsEqual(expected, kruskal.kruskal(graph,
            return_networkx_graph=True).edges(data=True))

if __name__ == '__main__':
    unittest.main()
