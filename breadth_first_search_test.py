#! usr/bin/python
"""Unit tests for breadth_first_search.py."""

import breadth_first_search
import networkx
import unittest

class BfsTest(unittest.TestCase):
    
    def testBreadthFirstSearch_UnweightedGraph(self):
        graph = networkx.Graph()
        graph.add_nodes_from([0, 9])
        graph.add_edges_from([
            (0, 1), (0, 2), (0, 3), (1, 3), (1, 6), (2, 4), (3, 9), (5, 6),
            (7, 8)])
        expected = [
                breadth_first_search.Vertex(0, None, 0),
                breadth_first_search.Vertex(1, 0, 1), 
                breadth_first_search.Vertex(2, 0, 1),
                breadth_first_search.Vertex(3, 0, 1),
                breadth_first_search.Vertex(6, 1, 2),
                breadth_first_search.Vertex(4, 2, 2),
                breadth_first_search.Vertex(9, 3, 2),
                breadth_first_search.Vertex(5, 6, 3)]
        component = breadth_first_search.breadth_first_search(graph, 0)
        # Convert list of Vertex objects to strings to compare using
        # assertItemsEqual.
        expected_str = [str(i) for i in expected]
        component_str = [str(i) for i in component]
        self.assertItemsEqual(expected_str, component_str)

if __name__ == '__main__':
    unittest.main()
