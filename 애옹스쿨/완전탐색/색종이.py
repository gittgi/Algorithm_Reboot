# 방법 1 : 색칠하기

arr = [[0] * 101 for _ in range(101)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1
ans = 0
for i in arr:
    ans += sum(i)

print(ans)


# 방법 2 : 좌표 확인하기

n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
ans = 0
for i in range(101):
    for j in range(101):
        for x, y in arr:
            if x <= i < x + 10 and y <= j < y + 10:
                ans += 1
                break

print(ans)