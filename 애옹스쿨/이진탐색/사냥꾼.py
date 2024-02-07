import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
sade = list(map(int, input().split()))
sade.sort()
animals = []
visited = [0] * (n)
for _ in range(n):
    x, y = map(int, input().split())
    animals.append((x, y))


for j in range(n):
    animal = animals[j]
    s = 0
    e = m-1
    while s <= e:
        mid = (s+e) // 2
        if abs(sade[mid] - animal[0]) + animal[1] <= k:
            visited[j] = 1
            break

        else:
            if sade[mid] == animal[0]:
                break
            elif sade[mid] > animal[0]:
                e = mid - 1
            else:
                s = mid + 1
    

print(sum(visited))
