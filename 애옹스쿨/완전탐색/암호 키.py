n = int(input())

for _ in range(n):
    num = int(input())

    for i in range(2, 10**6 + 1):
        if num % i == 0:
            print("NO")
            break
    else:
        print("YES")