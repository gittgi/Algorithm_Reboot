n, m = map(int, input().split())
arr = list(map(int, input().split()))
seg = [0] * (4*n)

def bigger(a, b):
    if a > b:
        return a
    return b

def init(node, start, end):
    if start == end:
        seg[node] = arr[start]
        return
    
    mid = (start + end) // 2
    
    init(node*2, start, mid)
    init(node*2 + 1, mid+1, end)

    seg[node] = bigger(seg[node*2], seg[node*2 + 1])

# node : 세그먼트트리 노드, start/end : arr 범위, t_start/t_end : 검사 범위
def check(node, start, end, t_start, t_end):
    # 아예 벗어남
    if t_start > end or t_end < start:
        return 0
    # 어긋남
    if start > end:
        return 0
    
    # 완전 포함
    if t_start <= start and end <= t_end:
        return seg[node]
    

    # 걸친 경우
    mid = (start + end) // 2
    return bigger(check(node*2, start, mid, t_start, t_end), check(node*2+1, mid+1, end, t_start, t_end))





init(1, 0, n-1)
ans = []
for i in range(m-1, n-m+1):
    ans.append(check(1, 0, n-1, i-m+1,i+m-1))

print(*ans)
    

