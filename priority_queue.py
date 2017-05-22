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
        if tasks_prios:
            for task, priority in tasks_prios:
                self.add_task(task, priority)

    def __str__(self):
        return str(self.pq)
    
    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def parent(self, i):
        return (i - 1) // 2 # Integer division

    def left_child(self, i):
        return 2*i + 1

    def right_child(self, i):
        return 2*i + 2

    def sift_up(self, i):
        parent = self.parent(i)
        priority_of_i = self.pq[i][1]
        priority_of_parent_of_i = self.pq[parent][1]

        if parent < 0:
            return
        while priority_of_i < priority_of_parent_of_i:
            self.swap(i, self.parent(i))
            i = parent
            parent = self.parent(i)
            priority_of_parent_of_i = self.pq[parent][1]
            if parent < 0:
                return

    def sift_down(self, i):
        while True:
            left_child = self.left_child(i)
            right_child = self.right_child(i)

            priority_of_i = self.pq[i][1]
            priority_of_left_child = self.pq[left_child][1]
            priority_of_right_child = self.pq[right_child][1]

            if (rigt_child < len(self.pq) and
                    priority_of_right_child < priority_of_left_child):
                child = right_child
                priority_of_child = priority_of_right_child
            else:
                child = left_child
                priority_of_child = priority_of_left_child

            if (child < len(self.pq) and
                    priority_of_child < priority_of_i):
                self.swap(i, child)
                i = child
            else:
                return

    def add(self, entry):
        self.pq.append(entry)
        self.sift_up(len(self.pq) - 1)

    def add_task(self, task, priority):
        if task in self.entry_finder:
            del self.entry_finder[task]
        entry = [task, priority]
        self.entry_finder[task] = entry
        self.add(entry)

    def pop(self):
        min_priority = self.pq[0]
        self.pq[0] = self.pq[-1]
        del self.pq[-1]
        self.sift_down(0)
        return min_priority
