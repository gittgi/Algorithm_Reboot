import sys
input = sys.stdin.readline

n, m = map(int, input().split())

player = [i for i in range(n)]

rank = [1 for i in range(n)]



def find(x, player):
    if player[x] == x:
        return x
    
    player[x] = find(player[x], player)
    return player[x]

def union(x, y, player, rank):
    x = find(x, player)
    y = find(y, player)
    
    if rank[x] < rank[y]:
        player[x] = y

    elif rank[x] > rank[y]:
        player[y] = x

    else:
        player[y] = x
        rank[x] += 1



for turn in range(m):

    a, b = map(int, input().split())
    a = find(a, player)
    b = find(b, player)
    if a == b:
        print(turn + 1)
        quit()
    else:
        union(a, b, player, rank)


print(0)