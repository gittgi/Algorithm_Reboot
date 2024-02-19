import sys
input = sys.stdin.readline
c = int(input())

for _ in range(c):
    d, n = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix = [0] * (n + 1)
   
    for i in range(1, n+1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
        
    ans = 0
    moduler_list = [0] * d
    for i in prefix:
        moduler_list[i % d] += 1  

    for i in moduler_list:
        if i <= 1:
            continue
        elif i == 2:
            ans += 1
        else:
            ans += (i * (i-1) // 2)
    
    print(ans)
