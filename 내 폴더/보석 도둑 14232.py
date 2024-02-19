

n = int(input())


ans = []

for i in range(2, int(n ** 0.5) + 1): # for문의 크기를 제곱근까지 줄여주는 것이 시간초과를 벗어나는 핵심
    while n % i == 0:
        ans.append(i)
        n //= i
if n != 1:
    ans.append(n)

print(len(ans))
print(*ans)
