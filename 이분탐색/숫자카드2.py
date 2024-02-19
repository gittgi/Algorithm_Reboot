import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

card.sort()

m = int(input())
query = list(map(int, input().split()))






def binary_search(arr, t, l, r):
    if l > r:
        return 0
    middle_idx = (l + r) // 2
    middle = arr[middle_idx]
    if t == middle:
        return arr[l:r+1].count(t)
    elif t > middle:
        return binary_search(arr, t, middle_idx + 1, r)
    else:
        return binary_search(arr, t, l, middle_idx - 1)

# 시간 초과...    
# ans = []
# for i in query:
#     ans.append(binary_search(card, i, 0, n-1))

# print(*ans)

  
n_dic = {}
for n in card:
    start = 0
    end = len(card) - 1
    if n not in n_dic:
        n_dic[n] = binary_search(card, n, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in query ))