arr = []

for i in range(10):
    arr.append(int(input()))

diff = 1000
now = 0
ans = 0
for i in arr:
    now += i
    if abs(100 - now) <= diff:
        ans = now
        diff = abs(100 - now)

print(ans)