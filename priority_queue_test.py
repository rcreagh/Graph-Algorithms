#! usr/bin/python
"""Unit tests associated with priority_queue.py

NOTE: This is WIP."""

import priority_queue
import unittest

class PriorityQueueTest(unittest.TestCase):
    
    def testPriorityQueue_DuplicateTask(self):
        queue = ([
            [0, 3],
            [1, 5],
            [2, 1],
            [1, 2]])

        self.assertRaises(priority_queue.PriorityQueueDuplicateTaskException,
                priority_queue.PriorityQueue(queue))
