n, k = map(int, input().split())
arr = [1, 2, 3]
ans = []
seq = 0

def recur(val):
    global seq, ans
    if val > n:
        return
    
    if val == n:
        seq += 1
        if seq == k:
            ans = list(map(str, ans))
            print("+".join(ans))
            quit()
    
    
    for i in range(3):
        ans.append(arr[i])
        recur(val + arr[i])
        ans.pop()

recur(0)
print(-1)


