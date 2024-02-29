# n = int(input())

# def check():
#     temp = ans[::-1]
#     for i in range(1, len(temp)):
#         # print(temp[:i], temp[i:2*i])
#         if temp[:i] == temp[i:2*i]:
#             return False
    
#     return True

# num = ["1", "2", "3"]
# ans = []
# def recur(cur):
#     if not check():
#         # print("here")
#         return
    
#     if cur == n:
#         print("".join(ans))
#         quit()
    
#     for i in num:
#         ans.append(i)
#         recur(cur+1)
#         ans.pop()


# recur(0)

import sys
input = sys.stdin.readline
n = int(input())
arr = [0 for _ in range(n)]
def check(cur, s):
    if cur <= 1:
        return True
    for i in range(1, n // 2 + 1):
        temp = s[:i]
        for j in range(i, n - i + 1, i):
            if temp == s[j:j + i]:
                return False
            temp = s[j:j + i]
            if temp == '0' * i:
                break
    return True
def recur(cur):
    if not check(cur, ''.join(map(str, arr))):
        return
    if cur == n:
        print(''.join(map(str, arr)))
        quit()
    for i in range(1, 4):
        arr[cur] = i
        recur(cur + 1)
        arr[cur] = 0
ans = []
recur(0)
