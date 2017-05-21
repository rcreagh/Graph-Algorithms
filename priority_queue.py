#! /usr/bin/python
"""This script is to create a class Priority Queue from scratch without the use
of Python's heapq library. 

NOTE: This is WIP."""

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
        parent = parent(i)
        priority_of_i = self.pq[i][0]
        priority_of_parent_of_i = self.pq[parent][0]

        if parent < 0:
            return
        while priority_of_i < priority_of_parent_of_i:
            swap(i, parent(i))
            i = parent
            parent = parent(i)
            if parent < 0:
                return

    def sift_down(self, queue, i):
        while True:
            left_child = left_child(queue, i)
            right_child = right_child(queue, i)

            priority_of_i = self.pq[i][0]
            priority_of_left_child = self.pq[left_child][0]
            priority_of_right_child = self.pq[right_child][0]

            if (rigt_child < len(queue) and
                    priority_of_right_child < priority_of_left_child):
                child = right_child
                priority_of_child = priority_of_right_child
            else:
                child = left_child
                priority_of_child = priority_of_left_child

            if (child < len(queue) and
                    priority_of_child < priority_of_i):
                swap(queue, i, child)
                i = child
            else:
                return

    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            del self.entry_finder[task]
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        add(self.pq, entry)

    def add(self, queue, task):
        self.pq.append(task)
        siftup(self.pq, len(self.pq) - 1)


