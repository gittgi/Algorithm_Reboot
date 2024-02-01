n, m = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

a = 0
b = 0

ans = []

while a < n and b < m:
    if arr_a[a] < arr_b[b]:
        ans.append(arr_a[a])
        a += 1
    elif arr_a[a] > arr_b[b]:
        ans.append(arr_b[b])
        b += 1
    else:
        ans.append(arr_a[a])
        ans.append(arr_b[b])
        a += 1
        b += 1

if a == n and b < m:
    ans += arr_b[b:]

elif b == m and a < n:
    ans += arr_a[a:]

print(*ans)


