import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    (a, b) = map(int, input().split())
    l = a - (b // 2)
    r = a + (b // 2)
    arr.append((l, r))

arr.sort()

