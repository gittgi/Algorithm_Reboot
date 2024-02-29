import sys
sys.setrecursionlimit(50010)

n = int(input())
arr = []

for _ in range(n):
    a,b  = map(int, input().split())
    arr.append((a, b))

sorted_arr = arr.sorted(key=lambda x: x[0])
# 제일 x 3개, y 3개, 작은 거 3개 3개 그리고 리저브 1개 1개 준비
# 걔네들이 있냐 없냐에 따라 좌표 변경하기





def recur(cur):
