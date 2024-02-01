
g = int(input())

now = 2
memory = 1

ans = []
while now <= 100000 and now != memory:
    # print("here")
    temp = now ** 2 - memory ** 2

    if temp == g:
        ans.append(now)
        memory += 1
    
    elif temp < g:
        now += 1

    else:
        memory += 1


if ans:
    for i in ans:
        print(i)
else:
    print(-1)