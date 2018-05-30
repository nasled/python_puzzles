#!/bin/python3

import math
import os
import random
import re
import sys
import heapq


class MedFinder:
    def __init__(self):
        # store bigger part
        self.min_heap = []
        # store lower part
        # store numbers as normalized negative numbers
        self.max_heap = []

    def peek_high(self):
        return self.min_heap[0]

    def peek_low(self):
        return self.max_heap[0] * -1

    def len_high(self):
        return len(self.min_heap)

    def len_low(self):
        return len(self.max_heap)

    def add(self, value):
        if self.len_low() == 0 or value < self.peek_low():
            heapq.heappush(self.max_heap, value * -1)
        else:
            heapq.heappush(self.min_heap, value)

    def rebalance(self):
        bigger = self.min_heap if self.len_high() > self.len_low() else self.max_heap
        lower = self.max_heap if self.len_high() > self.len_low() else self.min_heap
        if (len(bigger) - len(lower)) >= 2:
            heapq.heappush(lower, heapq.heappop(bigger) * -1)


    def med(self):
        bigger = self.min_heap if self.len_high() > self.len_low() else self.max_heap
        lower = self.max_heap if self.len_high() > self.len_low() else self.min_heap

        if len(bigger) == len(lower):
            res = (self.peek_high() + self.peek_low()) / 2
        else:
            res = bigger[0]

            if bigger == self.max_heap:
                res *= -1

        return round(float(res), 1)



med = MedFinder()
for i in [12,4,5,3,8,7]:
    med.add(i)
    med.rebalance()
    print(med.med())