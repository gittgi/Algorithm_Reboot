n = int(input())

arr = list(map(int, input().split()))

s = 0
e = n-1
ans = arr[s] + arr[e]
ans_s = s
ans_e = e

while s < e:
    temp = arr[s] + arr[e]

    if abs(temp) < abs(ans):
        ans = temp
        ans_s = s
        ans_e = e

    if temp == 0:
        break

    else:
        if temp > 0:
            e -= 1
        else:
            s += 1


print(arr[ans_s], arr[ans_e])