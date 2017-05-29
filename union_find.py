#! usr/bin/python
"""This script is a Python implementation of union-find, which is an efficient
way to determine if two nodes are in the same connected component. This is
created for use with Python's Networkx graph library.

NOTE: This is WIP and has not been tested yet."""

import networkx

class UnionFind:
    def __init__(self):
        self.roots = {}
        self.component_size = {}

    def find(self, node):
        """Finds the root node of the component containing the specified node.

        Args:
            node: Node which we want to find the root node of the component for.
        Returns:
            Root node of the component containing the specified node.
        """
        # If specified node is not in any seen component, set as a root and
        # return it (start a new component).
        if node not in self.roots:
            self.roots[node] = node
            self.component_size[node] = 1
            return node
        else:
            # If the root of the component of the specified node is itself,
            # return it.
            if self.roots[node] == node:
                return self.roots[node]
            # Otherwise, find the path of objects leading from the specified
            # node to the root and point all nodes directly to the root.
            else:
                path_to_root = [node]
                parent = self.roots[node]
                while path_to_root[-1] != parent:
                    path_to_root.append(parent)
                    parent = self.roots[parent]
        return parent

    def union(self, x, y):
        """Connects two components by pointing the root node of the smaller
        component to the root node of the larger component."""
        # Find roots of x and y
        roots = [self.find(n) for n in [x, y]]
        # Determine the larger component
        larger_component = max([(
            self.component_size[root], root) for root in roots])[1]
        for root in roots:
            if root != larger_component:
                self.component_size[
                        larger_component] += self.component_size[root]
                self.roots[root] = larger_component
