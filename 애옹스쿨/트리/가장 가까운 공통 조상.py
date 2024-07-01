import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

t = int(input())

def find_p(x):
    parent = []
    while x != 0:
        parent.append(x)
        x = arr[x]
    
    return parent[::-1]
            


for _ in range(t):
    n = int(input())
    arr = [0 for _ in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        arr[b] = a
    
    a, b = map(int, input().split())
    lst1 = find_p(a)
    lst2 = find_p(b)
    lst1.append(-1)
    lst2.append(-2)
    idx = 0
    while True:
        if lst1[idx] != lst2[idx]:
            print(lst1[idx-1])
            break
        idx += 1

    

    

