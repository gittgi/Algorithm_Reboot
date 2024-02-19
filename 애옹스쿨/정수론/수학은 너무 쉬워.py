import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

def soinsu(num):
    target = num
    prime_dict = dict()
    for k in range(2, num+1):
        if k * k > num:
            break
        while target % k == 0:
            if k in prime_dict:
                prime_dict[k] += 1
            else:
                prime_dict[k] = 1
            target //= k
    if target != 1:
        prime_dict[target] = 1
    return prime_dict

soinsu_dict_list = []

total_dict = dict()
for i in arr:
    soinsu_dict = soinsu(i)
    soinsu_dict_list.append(soinsu_dict)
    for j in soinsu_dict:
        if j in total_dict:
            total_dict[j] += soinsu_dict[j]
        else:
            total_dict[j] = soinsu_dict[j]


gcd = 1
gcd_dict = dict()
for i in total_dict:
    if total_dict[i] // n > 0:
        gcd_dict[i] = total_dict[i] // n
        gcd *= (i ** (total_dict[i] // n))

cnt = 0
for soinsu_dict in soinsu_dict_list:
    for i in gcd_dict:
        if i not in soinsu_dict:
            cnt += gcd_dict[i]
        else:
            if soinsu_dict[i] < gcd_dict[i]:
                cnt += (gcd_dict[i] - soinsu_dict[i])


print(gcd, cnt)



