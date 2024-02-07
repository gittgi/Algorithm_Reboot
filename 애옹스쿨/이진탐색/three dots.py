import sys
input = sys.stdin.readline


def binary_search(target, start, arr):
    s = start
    e = len(arr) - 1

    while s <= e:
        mid = (s+e) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            diff = arr[j] - arr[i]
            if binary_search(arr[j] + diff, j+1, arr):
                ans += 1
    print(ans)


