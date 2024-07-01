n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


arr.sort()
max_val = 0
for i in range(n):
    max_val = max((n - i) * arr[i], max_val)

print(max_val)