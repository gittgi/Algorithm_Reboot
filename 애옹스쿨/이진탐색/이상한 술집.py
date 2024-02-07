n , k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
# ans = 0
# for mak in range(1, sum(arr)):
#     jan = 0
#     for i in arr:
#         jan += i // mak
    
#     if jan < k:
#         continue
#     else:
#         ans = max(ans, mak)

# print(ans)

s = 1
e = sum(arr)
ans = 0

while s <= e:
    mid = (s + e) // 2
    jan = 0
    for i in arr:
        jan += i // mid
    
    if jan < k:
        e = mid - 1
    elif jan >= k:
        ans = max(ans, mid)
        s = mid + 1

print(ans)