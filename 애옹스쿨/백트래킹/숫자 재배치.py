numbers = input().split()
a = list(map(int, numbers[0]))
b = int(numbers[1])

ans = [0 for i in range(len(a))]
visited = [False for i in range(len(a))]
max_val = -1
def recur(cur):
    global max_val
    if cur == len(a):
        if ans[0] != 0:
            number = 0
            for i in range(len(ans)):
                number += ans[i] * (10 ** (len(ans) - 1 - i))
            if number < b:
                max_val = max(max_val, number)
        return
    
    for i in range(len(a)):
        if not visited[i]:
            visited[i] = True
            ans[cur] = a[i]
            recur(cur+1)
            visited[i] = False
    
recur(0)
print(max_val)