n = int(input())

arr1 = [[0] * 1001 for _ in range(1001)]
arr2 = [[0] * 1001 for _ in range(1001)]

pillar = []

for _ in range(n):
    pillar.append(tuple(map(int, input().split())))

pillar.sort()

for x, y in pillar:
    for i in range(x, 1001):
        for j in range(y):
            arr1[i][j] = 1

for x, y in pillar:
    for i in range(x+1):
        for j in range(y):
            arr2[i][j] = 1
ans = 0 
for i in range(1001):
    for j in range(1001):
        if arr1[i][j] == 1 and arr2[i][j] == 1:
            ans += 1

print(ans)