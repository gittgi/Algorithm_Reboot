n , s = map(int, input().split())

arr = list(map(int, input().split()))



for i in range(1, n):
    arr[i] = arr[i] +arr[i-1]

arr = [0] + arr

left = 0
right = 1
min_len  = n + 1


while right < n+1:
    if left == right:
        right += 1
        continue
    if s <= arr[right] - arr[left]:
        min_len = min(min_len, right - left) 
        left += 1
    else:
        right += 1

if min_len == n+1: print(0)
else: print(min_len)