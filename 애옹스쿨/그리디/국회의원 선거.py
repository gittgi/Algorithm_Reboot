n = int(input())
arr = []
me = int(input())
for i in range(n - 1):
    arr.append(int(input()))
arr.sort(reverse=True)
cnt = 0

if len(arr) == 0:
    print(0)
    quit()

while arr[0] >= me:

    cnt += 1
    arr[0] -= 1
    me += 1
    arr.sort(reverse=True)

print(cnt)
    
    