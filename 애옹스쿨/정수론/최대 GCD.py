n = int(input())

def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


for _ in range(n):
    ans = 0
    arr = list(map(int, input().split()))
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            ans = max(ans, get_gcd(arr[i], arr[j]))

    print(ans)