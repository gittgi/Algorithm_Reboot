# 바운드로 풀기
import sys
input = sys.stdin.readline 
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
cards.sort()
ans = []
for i in range(m):
    s = 0
    e = n-1
    l = -1

    while s <= e:
        mid = (s+e) // 2

        if cards[mid] >= arr[i]:
            l = mid
            e = mid - 1
         
        else:
            s = mid + 1
    


    s = 0
    e = n-1
    u = -1

    while s <= e:
        mid = (s+e) // 2
        if cards[mid] <= arr[i]:
            u = mid+1
            s = mid+1

        else:
      
            e = mid -1
    if l == -1 or u == -1:
        ans.append(0)
    else:
        ans.append(u - l)

print(*ans)