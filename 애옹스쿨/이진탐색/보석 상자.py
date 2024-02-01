n, m = map(int, input().split())
arr = []
for i in range(m):
    arr.append(int(input()))




# for i in range(1, max(arr)):
#     people = 0
#     for j in arr:
#         if j % i == 0:
#             people += j // i
#         else:
#             people += (j // i) + 1
    
#     if people > n:
#         continue
#     else:
#         print(i)
#         quit()


s = 1
e = max(arr)
l = -1
ans = 0
while s <= e:
    mid = (s+e) // 2
    people = 0
    for j in arr:
        if j % mid == 0:
            people += j // mid
        else:
            people += (j // mid) + 1
    if people > n:
        s = mid + 1
    else:
        ans = mid
        e = mid - 1

print(ans)