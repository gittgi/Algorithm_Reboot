# 에라토스테네스의 체로 4000000까지의 소수 구하기
n = int(input())
isPrime = [True for _ in range(n + 1)]

isPrime[1] = False

for i in range(2, n + 1):
    if isPrime[i] == False:
        continue

    for j in range(i*i, n + 1, i):

        isPrime[j] = False

prime_list = []

for i in range(1, n + 1):
    if isPrime[i] == True:
        prime_list.append(i)
prime_list += [0]
ans = 0

s = 0
e = 0
total = prime_list[0]


while e < len(prime_list)-1 and s <= e:
    if total == n:
        ans += 1
        total -= prime_list[s]
        s += 1
        e += 1
        total += prime_list[e]
    
    elif total < n:
        e += 1

        total += prime_list[e]

    else:
        total -= prime_list[s]
        s += 1


print(ans)
