gcd, lcm = map(int, input().split())
total = gcd * lcm

def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


for i in range(int(total**(0.5)), 0, -1):
    if total % i == 0:
        if get_gcd(i, total//i) == gcd:
            print(i, total // i)
            break
