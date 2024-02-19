import sys
input = sys.stdin.readline

tc = int(input())


# 여기 벨만-포드에서 inf를 쓰면 안되는 이유
# 단절된 그래프의 경우, 시작점을 1로 잡았을 때, 2와 3 사이에서 싸이클이 생겨도 2와 3은 업데이트되지 않고 계속 지나친다
# 따라서 정상 종료되기 때문에 사이클을 판별 할 수 없음...
# https://www.acmicpc.net/board/view/50494 
def bellman(x):
    bmf = [1e9] * (n+1)
    bmf[x] = 0
    for i in range(n):
        
 
        for j in range(m+m+w):
            start = arr[j][0]
            end = arr[j][1]
            dist = arr[j][2]
        
            if bmf[end] > bmf[start] + dist:

                bmf[end] = bmf[start] + dist
                if i == n-1:
                    return True

    return False




for _ in range(tc):
    n, m, w = map(int, input().split())

    arr = []
    for k in range(m):
        a, b, d = map(int, input().split())
        arr.append((a, b, d))
        arr.append((b, a, d))

    for l in range(w):
        a, b, d = map(int, input().split())
        arr.append((a, b, -d))

 

  

    if bellman(1):
        print("YES")
    else:
        print("NO")

