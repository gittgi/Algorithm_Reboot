def soinsu(num):
    x = num
    numbers = set()
    for l in range(2, num+1):
        if l * l > num:
            break
        cnt = 0
        while x % l == 0:
            cnt += 1
            x //= l
        if cnt != 0:
            numbers.add((l, cnt))
    
    if x != 1:
        numbers.add((x, 1))
    
    return numbers


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    num_arr = soinsu(k)
    min_val = float("inf")
    for p, sqr in num_arr:
        cnt = 0
        for i in range(1, 1 + 10 ** 18):
            if p ** i > n:
                break
            cnt += n // (p ** i)
        cnt //= sqr # 이거 안나눠떨어졌으면 어떡함...
        min_val = min(min_val, cnt)
    print(min_val)

