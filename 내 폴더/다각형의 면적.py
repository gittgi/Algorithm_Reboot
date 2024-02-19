import sys
input = sys.stdin.readline

n = int(input())

x_list = []
y_list = []


for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_list.append(x_list[0])
y_list.append(y_list[0])

first = 0
second = 0
for i in range(n):
    first += (x_list[i] * y_list[i+1])

for j in range(n, 0, -1):
    second += (x_list[j] * y_list[j-1])

ans = abs(first - second) / 2

print(round(ans, 1))

# 신발끈 공식 이용..