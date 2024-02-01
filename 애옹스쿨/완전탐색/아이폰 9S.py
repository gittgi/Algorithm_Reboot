arr = []
num_set = set()

n = int(input())



for _ in range(n):
    num = int(input())
    arr.append(num)
    num_set.add(num)

max_cnt = 1
for i in num_set:
    prev = -1
    cnt = 0
    for num in arr:
        if num == i:
            continue
        if prev == num:      
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
        prev = num
        max_cnt = max(max_cnt, cnt)


print(max_cnt)