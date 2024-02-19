import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
    




g = int(input())
p = int(input())
par = [i for i in range(g+1)]

cnt = 0


for _ in range(p):
    i = int(input())
    k = find(i) # find 함수를 통해 부모(k-1) 가 차있는지를 확인하게 할 수 있다. 만약 k-1로 이어지지 않고 자기 자신(k)을 가리키고 있다면, 거기다 주차한 후에 부모를 다시 k-1로 연결 시켜주는 것으로 자기보다 낮은 포트 검색을 계속 해나갈 수 있다.
    if k == 0: # 1 포트의 부모가 0일 것이기 때문에, 0까지 전부 차있다는 뜻이 된다.
        break
    par[k] = k-1  # 자신의 바로 아래 포트를 부모로 연결하는 것으로, find함수를 통해 자신 이하의 포트의 가능 여부를 모두 확인 할 수 있다
    cnt += 1

print(cnt)