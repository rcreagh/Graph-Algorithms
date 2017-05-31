#! usr/bin/python
"""Unit tests for union_find.py

NOTE: This is WIP."""

import union_find
import unittest

class UntionFindTest(unittest.TestCase):

    def testFind(self):
        ufs = union_find.UnionFind()
        ufs.roots = {}
        ufs.roots[0] = 1
        ufs.roots[1] = 2
        ufs.roots[2] = 5
        ufs.roots[3] = 4
        ufs.roots[4] = 4
        ufs.roots[5] = 5
        
        parents = []
        for i in range(0, 6):
            parents.append(ufs.find(i))

        expected = [5, 5, 5, 4, 4, 5]

        self.assertEqual(expected, parents)
        
if __name__ == '__main__':
    unittest.main()
