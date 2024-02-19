n, d, k, c = map(int, input().split())


arr = []

for _ in range(n):
    arr.append(int(input()))

arr += arr[:]

s = 0
e = k - 1
visited = [0] * (d+1)


for i in range(k):
    visited[arr[i]] += 1

visited[c] += 1

sushi = 0
for i in range(d+1):
    if visited[i] > 0:
        sushi += 1

ans = sushi

while e < len(arr)-1:
    e += 1
    visited[arr[e]] += 1
    if visited[arr[e]] == 1:

        sushi += 1

    visited[arr[s]] -= 1
    if visited[arr[s]] == 0:

        sushi -= 1
    s += 1


    if ans < sushi:
        ans = sushi


    


    

print(ans)
