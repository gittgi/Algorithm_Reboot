import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("2.in")
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
num = 15
prefix = [0] * (2 + num)
suffix = [0] * (2 + num)

idx = 0
for i in range(num + 1):
    if i != 0:
        prefix[i] = prefix[i - 1] + idx
    
    while idx < n and arr[idx] == i:
        idx += 1

idx = n - 1
for i in range(num, -1, -1):
    suffix[i] = suffix[i + 1] + n - idx - 1
    
    while idx >= 0 and arr[idx] == i:
        idx -= 1
print(prefix)
print(suffix)


def calculate_distance(target, l, r):

    left = l * prefix[target]
 
    right = r * suffix[target]

    return left + right




# def bin_search(start, end, l, r):
#     if start >= end:
#         return start

#     mid = (start + end) // 2    

#     left_len = index_bin_search(mid)
    
#     now = calculate_distance(mid, left_len, l, r)
#     right = calculate_distance(mid + 1,left_len, l, r)

#     if now <= right:
#         return bin_search(start, mid, l, r)
#     else:
#         return bin_search(mid+1, end, l, r)

def bin_search(start, end, l, r):
    while start < end:
        mid = (start + end) // 2
  
        now = calculate_distance(mid, l, r)
        right = calculate_distance(mid + 1, l, r)
        if now <= right:
            end = mid
        else:
            start = mid + 1
    return start

q = int(input())

for _ in range(q): 
    l, r = map(int, input().split())

    # 이분탐색으로 Target 찾기
    target = bin_search(0, num, l, r)

    print(calculate_distance(target, l, r))
    
    