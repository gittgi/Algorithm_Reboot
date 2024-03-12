import sys
input = sys.stdin.readline
sys.setrecursionlimit(150010)


n = int(input())
arr = list(map(int, input().split()))
m = int(input())

dp = [[-1 for i in range(m+1)] for j in range(3)]

# cur는 현재 어디를 보고 있는지, train은 현재 기관차, contain은 현재 기관차가 몇개 들고 있는지 
def recur(cur, train, contain):
    if contain > m:
        return -(1 << 60)
    
    if cur == n:
        return 0
    
    if train == 3:
        return 0
    
    if dp[train][contain] != -1:
        return dp[train][contain]
    

    
    
    passenger = 0
    # 현재 기관차가 이번 객차를 포함한다.
    passenger = max(recur(cur+1, train, contain + 1) + arr[cur], passenger) 

    # 현재 기관차가 이번 객차를 포함하지 않는다.
    # 이미 포함한 객차가 있다면, 다음 기관차로 넘겨주기 (다음 기관차가 현재 객체를 한번 더 체크)
    if contain > 0:
        passenger = max(recur(cur, train+1, 0), passenger)
    # 아직 포함한 객차가 없다면, 다음 기관차로 넘겨주지 않기 
    else:
        passenger = max(recur(cur + 1, train, 0), passenger)
    
    dp[train][contain] = passenger
    return dp[train][contain]




print(recur(0, 0, 0))