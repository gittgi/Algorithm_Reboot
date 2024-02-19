tc = int(input())

def bin_search(l,r,t):
    while l<=r:
        m = (l+r)//2
        if arr[m] == t:
            return 1
        if arr[m] > t:
            r = m-1
        else:
            l = m+1
    return 0

for t in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    ans = 0
    for i in range(len(arr) - 2):
        first = arr[i]
        
        for j in range(i+1, len(arr) - 1):
            second = arr[j]

            if bin_search(j+1, len(arr) -1, second + second - first):
                ans += 1
    
    print(ans)

# 시간초과..            
# def binary_search(l, r, target):
#     if l > r:
#         return False
    
#     middle = (l + r) // 2

#     if arr[middle] == target:
#         return True
    
#     if arr[middle] > target:
#         return binary_search(l, middle-1, target)
#     else:
#         return binary_search(middle + 1, r, target)

