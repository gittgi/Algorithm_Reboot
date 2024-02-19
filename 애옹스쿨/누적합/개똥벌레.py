n, h = map(int, input().split())

imos = [0] * h

for i in range(n):
    l = int(input())
    if i % 2:
        imos[0] += 1
        imos[l] -= 1
    
    else:
        imos[h - l] += 1

prefix = [0] * (h+1)

for i in range(1, h+1):
    prefix[i] = prefix[i-1] + imos[i-1]

ans = min(prefix[1:])
cnt = prefix[1:].count(ans)

print(ans, cnt)
