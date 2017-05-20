#! /usr/bin/python
"""This script is to create a class Priority Queue from scratch without the use
of Python's heapq library. """

import itertools

class PriorityQueue:
    """Priority queue implementation."""

    def __init__(self, tasks_prios = None):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()
        if tasks_prios:
            for task, priority in tasks_prios:
                self.add_task(task, priority)

    def parent(self, i):
        return (i - 1) // 2 # Integer division

    def left_child(self, i):
        return 2*i + 1

    def right_child(self, i):
        return 2*i + 2

    def sift_up(self, i):
        if i == 0:
            return 0
        priority_of_i = self.pq[i][0]
        priority_of_parent_of_i = self.pq[parent(i)][0]

        while priority_of_i < priority_of_parent_of_i:
            pass

    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            del self.entry_finder[task]
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heap(self.pq, entry)

    def heap(self, queue, queue_entry):


