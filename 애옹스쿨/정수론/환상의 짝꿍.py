

isPrime = [True for i in range(2*(10**6) + 1)]
isPrime[1] = False
for i in range(2, 2*(10**6) + 1):
    if not isPrime[i]:
        continue
    for j in range(i * i, 2*(10**6) + 1, i):
        isPrime[j] = False

sosu = []
for i in range(1, 2*(10**6) + 1):
    if isPrime[i]:
        sosu.append(i)

def sosu_pandan(x):
    for i in sosu:
        if x % i == 0:
            return False
    return True
    




n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    total = a+ b
    if total != 2 and total % 2 == 0:
        print("YES")
    elif total % 2 == 1:
        if total - 2 > (2*(10**6)+1):
            if sosu_pandan(total-2):
                print("YES")
            else:
                print("NO")
        else:
            if isPrime[total-2]:
                print("YES")
            else:
                print("NO")
    
    else:
        print("NO")


        
   
