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

    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            del self.entry_finder[task]
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        #TODO: Add heapify here

