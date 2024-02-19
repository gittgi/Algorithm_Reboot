n = int(input())

cnt = 0
for i in range(1, n+1):
    number = i
    if len(str(number)) <= 2:
        cnt += 1
    else:
        prev = int(str(number)[1])
        diff = int(str(number)[1]) - int(str(number)[0])
        for j in range(2, len(str(number))):
            if int(str(number)[j]) - prev != diff:
                break
            else:
                prev = int(str(number)[j])
        else:
            cnt += 1


print(cnt)