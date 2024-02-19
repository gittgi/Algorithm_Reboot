import sys
input = sys.stdin.readline
from collections import deque

dance = [0] + list(map(int, input().split()))
length = len(dance)

def move(start, end):
    if start == end:
        return 1
    elif start == 0:
        return 2
    else:
        if start == 1:
            if end == 2: return 3
            elif end == 3: return 4
            elif end == 4: return 3
        elif start == 2:
            if end == 3: return 3
            elif end == 4: return 4
            elif end == 1: return 3
        elif start == 3:
            if end == 4: return 3
            elif end == 1: return 4
            elif end == 2: return 3
        elif start == 4:
            if end == 1: return 3
            elif end == 2: return 4
            elif end == 3: return 3



