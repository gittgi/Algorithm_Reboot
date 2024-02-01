# 에라토스테네스의 체
a, b = map(int, input().split())

def find_2(n):

    cnt_2 = 0
    for i in range(1, 10**15 + 1):
        if 2 ** i > n:
            return cnt_2

        cnt_2 += (n // (2**i))

odd = 0
if a % 2 == 0:
    if b % 2 == 0:
        odd = (b - a) // 2
    else:
        odd = 1 + (b-a) // 2
else:
    odd = 1 + (b-a) // 2
    

print(2 ** (find_2(b) - find_2(a-1)) + odd)
