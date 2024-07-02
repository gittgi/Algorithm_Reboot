k = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(k)]



def recur(s, e, depth):
    if s == e:
        tree[depth].append(arr[s])
        return
    
    m = (s + e) // 2
    tree[depth].append(arr[m])
    recur(s, m-1, depth + 1)
    recur(m+1, e, depth + 1)

recur(0, len(arr)-1, 0)
for i in tree:
    print(*i)