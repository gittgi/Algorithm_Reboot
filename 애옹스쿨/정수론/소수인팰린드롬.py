
a, b = map(int, input().split())

isPrime = [True for i in range(b+1)]
isPrime[1] = False

for i in range(2, b+1):
    if not isPrime[i]:
        continue
    for j in range(i * i, b+1, i):
        isPrime[j] = False

for i in range(a, b+1):
    if isPrime[i]:
        str_i = str(i)
        for j in range(len(str_i) // 2):
            if str_i[j] != str_i[-j - 1]:
                break
        else:
            print(i)
        

print(-1) 
