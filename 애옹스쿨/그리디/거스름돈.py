# 각 단위가 배수관계라면 그리디 ㄱㄱ

coins = [500, 100, 50, 10, 5, 1]

n = int(input())
n = 1000 - n
coin = 0

for i in coins:
    coin += (n // i)
    n = n % i

print(coin)
