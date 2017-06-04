#! usr/bin/python
"""Unit tests for union_find.py."""

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

    def testUnion(self):
        ufs = union_find.UnionFind()
        ufs.union(0, 1) # Point 0 to root 1.
        ufs.union(0, 2) # Point 2 to root of 0 (1).
        ufs.union(3, 4) # Point 3 to root 4.
        ufs.union(4, 5) # Point 5 to root of 4 (4).
        ufs.union(2, 3) # Point path from 2 to root of 2 (1) to root of 3 (4).

        parents = []
        for i in range (0, 6):
            parents.append(ufs.roots[i])

        expected = [1, 4, 1, 4, 4, 4]
        self.assertEqual(expected, parents)

if __name__ == '__main__':
    unittest.main()
