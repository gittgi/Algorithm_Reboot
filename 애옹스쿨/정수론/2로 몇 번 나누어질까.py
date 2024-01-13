def f(k):
    cnt = 0

    for i in range(1, k):
        if 2 ** i > k:
            break
        
        cnt += k // 2
    
    return 2 ** cnt


print(f(15))
print(f(40))