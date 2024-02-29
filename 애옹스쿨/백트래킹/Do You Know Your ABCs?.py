'''
4 5 7 8
a, b, c, a + b, a + c, b + c, a + b + c
각각 매칭시켜보고 되는가 안되는가 판단
'''


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))