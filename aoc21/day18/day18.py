import itertools
import math
from functools import reduce
from os import path


def add_left(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [add_left(x[0], n), x[1]]


def add_right(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [x[0], add_right(x[1], n)]


def explode(x, n=4):
    if isinstance(x, int):
        return False, None, x, None
    if n == 0:
        return True, x[0], 0, x[1]
    a, b = x
    exp, u, a, v = explode(a, n - 1)
    if exp:
        return True, u, [a, add_left(b, v)], None
    exp, u, b, v = explode(b, n - 1)
    if exp:
        return True, None, [add_right(a, u), b], v
    return False, None, x, None


def split(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, math.ceil(x / 2)]
        return False, x
    a, b = x
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]


def add(a, b):
    x = [a, b]
    while True:
        change, _, x, _ = explode(x)
        if change:
            continue
        change, x = split(x)
        if not change:
            break
    return x


def magnitude(x):
    if isinstance(x, int):
        return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])
   

if __name__ == "__main__":
    file1 = open('day18.txt', 'r')
    lines = list(map(eval, file1.read().splitlines()))
    print("Part 1:", magnitude(reduce(add, lines)))
    print(
        "Part 2:",
        max(magnitude(add(a, b)) for a, b in itertools.permutations(lines, 2)),
    )



