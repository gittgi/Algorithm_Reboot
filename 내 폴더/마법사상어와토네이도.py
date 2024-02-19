import math, sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


x, y = (N - 1) // 2, (N - 1) // 2

count = 0
turn = 1
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
d = 0
ans = 0

def valid(x, y, sand):
    global ans
    if 0 <= x < N and 0 <= y < N:
        arr[x][y] += math.floor(sand)
        return True
    else:
        ans += math.floor(sand)
        return False


tornado = [
    [(-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (0, -2, 0.05),(0, -1, 'a'), (0, 1, 0), (0, 2, 0), (1, -1, 0.1), (1, 0, 0.07),(1, 1, 0.01),(2, 0, 0.02)],
    [(-2, 0, 0), (-1, -1, 0.01), (-1, 0, 0), (-1, 1, 0.01), (0, -2, 0.02),(0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (1, -1, 0.1), (1, 0, 'a'),(1, 1, 0.1),(2, 0, 0.05)],
    [(-2, 0, 0.02), (-1, -1, 0.01), (-1, 0, 0.07), (-1, 1, 0.1), (0, -2, 0),(0, -1, 0), (0, 1, 'a'), (0, 2, 0.05), (1, -1, 0.01), (1, 0, 0.07),(1, 1, 0.1),(2, 0, 0.02)],
    [(-2, 0, 0.05), (-1, -1, 0.1), (-1, 0, 'a'), (-1, 1, 0.1), (0, -2, 0.02),(0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (1, -1, 0.01), (1, 0, 0),(1, 1, 0.01),(2, 0, 0)]]

def sand_blow(x, y, dirc):
    sand = arr[x][y]
    arr[x][y] = 0
    blown = 0
    for dx, dy, d in tornado[dirc]:
        if d == 'a':
            lx, ly = dx, dy
            continue
        else:
            blown += math.floor(sand * d)
            valid(x+dx, y+dy, sand * d)

    valid(x + lx, y + ly, sand - blown)


while not ( N // 2 + 1 == turn and d == 1 ):
 
    if d <= 1:
        if count < (2 * turn) - 1:
            dx, dy = direction[d]
            x += dx
            y += dy
            # 요기에 모래 나누기 로직
            sand_blow(x, y, d)
 
            count += 1
        else: 
            d = (d + 1) % 4
            count = 0
    else:
        if count < (2 * turn):
            dx, dy = direction[d]
            x += dx
            y += dy
            # 요기에 모래 나누기 로직
            sand_blow(x, y, d)

            count += 1
        else:
            if d == 3:
                turn += 1
            d = (d + 1) % 4
            count = 0


print(ans)