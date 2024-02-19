import sys
input = sys.stdin.readline

n, m = map(int, input().split())

truth_people = list(map(int, input().split()))

truth_people = truth_people[1:]

truth_visited = [False] * (n+1)



people = [i for i in range(n+1)]
rank = [1] * (n+1)

def find(x):
    if people[x] == x:
        return x
    people[x] = find(people[x])
    return people[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if rank[x] > rank[y]:
        people[y] = x
        rank[x] = rank[y] + 1
    elif rank[x] < rank[y]:
        people[x] = y
        rank[y] = rank[x] + 1
    else:
        people[y] = x
        rank[x] += 1

party = []

for _ in range(m):
    temp = list(map(int, input().split()))
    k = temp[0]
    party.append(temp[1:])
    for i in range(1, k+1):
        union(temp[1], temp[i])

for i in truth_people:
    truth_visited[find(i)] = True



ans = 0 

for i in party:
    for j in i:
        if truth_visited[find(j)] == True:
            break
    else:
        ans += 1




print(ans)
