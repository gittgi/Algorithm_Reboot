import sys
input = sys.stdin.readline


def dfs(x, y, stage):
    global max_val
    max_val = max(stage, max_val)

    for dx, dy in delta:
        if R > x + dx >= 0 and C > y + dy >= 0:
            idx = ord(arr[x+dx][y+dy]) - ord('A')
            if letter[idx] == 0:
                letter[idx] = 1

                dfs(x+dx, y+dy, stage+1)
                letter[idx] = 0


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]


letter = [0] * 26

max_val = 0
letter[ord(arr[0][0]) - ord('A')] = 1

dfs(0, 0, 1)
print(max_val)
