#! /usr/bin/python
"""This script is to create a class Priority Queue from scratch without the use
of Python's heapq library. This is for learning purposes, to demonstrate how a
Priority Queue is built from scratch. Of course, in practice, we would just use
the heapq library."""

import itertools

class PriorityQueueDuplicateTaskException(Exception):
    """An exception for when the same task is entered the queue more than
    once."""
    pass

class DataTypeException(Exception):
    """An exception for when the priority of a node is entered as a string."""
    pass

class EmptyPriorityQueueException(Exception):
    """An exception for when 'pop' is called on an empty queue."""
    pass

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
        """Defines Parent node of a given node in the heap structure."""
        return (i - 1) // 2

    def left_child(self, i):
        """Defines the left child of a given node in the heap structure."""
        return 2*i + 1

    def right_child(self, i):
        """Defines the right child of a given node in the heap structure."""
        return 2*i + 2

    def sift_up(self, i):
        """Compares a node with its parent in the heap structure. Swaps if its
        priority is lower than that of its parent and repeats."""
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
        """Compares a node with its children in the heap structure. Swaps if
        its priority is higher than that of either of its children. If its
        priority is higher than that of both of its children, swaps with the
        child with lower priority."""
        while True:
            left_child = self.left_child(i)
            right_child = self.right_child(i)
            priority_of_i = self.pq[i][1]
            try:
                priority_of_left_child = self.pq[left_child][1]
            except:
                return
            try:
                priority_of_right_child = self.pq[right_child][1]
            except:
                priority_of_right_child = float('inf')

            if (right_child < len(self.pq) and
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

    def add_task(self, task, priority):
        """Adds a task to existing priority queue."""
        if isinstance(priority, str):
            raise DataTypeException(
                    "Priority must be a number - string entered.")
        if task in self.entry_finder:
            raise PriorityQueueDuplicateTaskException(
                    "Duplicate task entered into priority queue.")
        entry = [task, priority]
        self.entry_finder[task] = entry
        self.pq.append(entry)
        self.sift_up(len(self.pq) - 1)

    def pop(self):
        """Pops task with lower priority off the heap."""
        if not self.pq:
            raise EmptyPriorityQueueException(
                    "Attempted to pop task from an empty queue.")
        min_priority = self.pq[0]
        self.pq[0] = self.pq[-1]
        del self.pq[-1]
        self.sift_down(0)
        return min_priority
