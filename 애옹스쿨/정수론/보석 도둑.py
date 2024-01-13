n = int(input())

ans = []

x = n
for i in range(2, n + 1):

    if i * i > n:
        break

    while x % i == 0:
        ans.append(i)
        x //= i

if x != 1:
    ans.append(x)

print(len(ans))
print(*ans)