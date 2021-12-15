from collections import defaultdict, Counter, deque
from itertools import pairwise
import functools
import math
from heapq import heappop, heappush
from pprint import pprint

def shortest_distance(data, t):
    heap = [(0, 0, 0)]
    seen = {(0, 0)}
    while heap:
        distance, x, y = heappop(heap)
        if x == t * len(data) - 1 and y == t * len(data[0]) - 1:
            return distance

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x_, y_ = x + dx, y + dy
            if x_ < 0 or y_ < 0 or x_ >= t * len(data) or y_ >= t * len(data):
                continue
            
            # quotient and remainder
            a, am = divmod(x_, len(data))
            b, bm = divmod(y_, len(data[0]))
            # subtracted 1 to exclude the start
            n = ((data[am][bm] + a + b) - 1) % 9 + 1

            if (x_, y_) not in seen:
                seen.add((x_, y_))
                heappush(heap, (distance + n, x_, y_))



if __name__ == "__main__":
    with open("day15.txt") as f:
        data = [list(map(int, line)) for line in f.read().strip().split("\n")]

        print(shortest_distance(data, 1))
        print(shortest_distance(data, 5))