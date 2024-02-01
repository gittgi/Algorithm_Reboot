import sys
input = sys.stdin.readline
n = int(input())
sanguen = list(map(int, input().split()))

m = int(input())

arr = list(map(int, input().split()))
sanguen.sort()


ans = []
for i in arr:
    s = 0
    e = n-1

    while s <= e:
        mid = (s + e) //2

        if sanguen[mid] == i:
            ans.append(1)
            break

        elif sanguen[mid] > i:
            e = mid - 1
        
        else:
            s = mid +1
    
    else:
        ans.append(0)

print(*ans)