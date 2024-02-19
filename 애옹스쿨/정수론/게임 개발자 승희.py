import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
numbers =[0] * n

arr = list(map(int, input().split()))
adds = [0] * m
adds[0] = arr[0] % 7

remain = set()
for i in range(n):
    temp = nums[i] % 7
    if temp == 0:
        numbers[i] = 7
    else:
        numbers[i] = temp
    remain.add(numbers[i])

for i in range(1, m):
    adds[i] = (adds[i-1] + arr[i]) % 7

visited = [0] * n
not_to_add_idx = []
for i in range(m):
    to_add = adds[i]
    if len(remain) == 0:
        break
    if 7 - to_add in remain:
        if len(remain) == 1:
            not_to_add_idx.append(i)
            continue
        else:
            remain.remove(7 - to_add)
            for j in range(n):
                if numbers[j] == 7 - to_add:
                    visited[j] = 1 # 지워졌다는 뜻

total = 0
for i in range(m):
    if i not in not_to_add_idx:
        total += arr[i]

ans = []
for i in range(n):
    if visited[i] == 0:
        ans.append(nums[i] + total)

print(len(ans))
print(*ans)