n = int(input())

names = dict()
cnt = 0
for i in range(n):
    name, pm = input().split()
    if name in names:
        if pm == "+":
            names[name] += 1
        else:
            if names[name] - 1 < 0:
                cnt += 1
            else:
                names[name] -= 1
    else:
        if pm == "+":
            names[name] = 1
        else:
            names[name] = 0
            cnt += 1
        

for name in names:
    cnt += names[name]

print(cnt)
