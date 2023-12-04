# 세그먼트 트리

# 시간 초과 컷이 빡빡하기 떄문에, 곱셈 계산 대신 1, 0, -1로만 & 값을 return헤서 그걸로 만들고 하기 보다는, 배열에 직접 입력하고, 다시 그걸 조회해서 만드는 방법

def make_seg(node, start, end):
    if start == end:
        if arr[start] > 0:
            seg[node] = 1
        elif arr[start] < 0:
            seg[node] = -1
        else: 
            seg[node] = 0
        return

    mid = (start + end) // 2

    make_seg(2 * node, start, mid)
    make_seg((2 * node) + 1, mid + 1, end)

    seg[node] = seg[2*node] * seg[2*node + 1]



def check(target_start, target_end, node, start, end):

    # 엇갈리는 경우
    if target_start > target_end:
        return 1

    # 아예 벗어나는 경우
    if target_end < start or target_start > end:
        return 1
    
    # 딱 포함되는 경우
    if target_start <= start and end <= target_end:
        if seg[node] > 0:
            return 1
        elif seg[node] < 0:
            return -1
        else:
            return 0

    # 걸치는 경우들
    mid = (start + end) // 2
    left = check(target_start, target_end, node * 2, start, mid)
    right = check(target_start, target_end, (node * 2) + 1, mid + 1, end)

    return left * right


def update(node, start, end, target, target_val):
    # 관련 없는 노드는 그냥 반환
    if target < start or target > end:
        return
    
    # 업데이트 대상 노드의 경우 업데이트
    if start == end:
        if target_val > 0:      
            seg[node] = 1
        elif target_val < 0:
            seg[node] = -1
        else:
            seg[node] = 0
        return
    
    mid = (start + end) // 2
    update(node * 2, start, mid, target, target_val)
    update((node * 2) + 1, mid + 1, end, target, target_val)
    seg[node] = seg[2*node] * seg[2*node + 1]
    return

while True:
    try:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        seg = [1] * (4 * n)
        make_seg(1, 0, n - 1)

        ans = ""
        for i in range(k):
            cmd, s, e = input().split()

            if cmd == "C":
                update(1, 0, n-1, int(s)-1, int(e))
            else:
                val = check(int(s)-1, int(e)-1, 1, 0, n-1)
                if val > 0:
                    ans += "+"
                elif val < 0:
                    ans += "-"
                else:
                    ans += "0"
        print(ans)
        # print(seg)
    except Exception:
        break
    


