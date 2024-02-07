import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
B.sort()
C.sort()
def find_from_B(x):
    s = 0
    e = b-1
    while s <= e:
        mid = (s+e) // 2
        if B[mid] == x:
            return x
        elif B[mid] > x:
            e = mid-1
        else:
            s = mid+1

    if s == b:
        return B[-1]
    elif e == -1:
        return B[0]
    else:
        if abs(x - B[s]) > abs(x - B[e]):
            return B[e]
        else:
            return B[s]
def find_from_C(x):
    s = 0
    e = c-1
    while s <= e:
        mid = (s+e) // 2
        if C[mid] == x:
            return x
        elif C[mid] > x:
            e = mid-1
        else:
            s = mid+1

    if s == c:
        return C[-1]
    elif e == -1:
        return C[0]
    else:
        if abs(x - C[s]) > abs(x - C[e]):
            return C[e]
        else:
            return C[s]
        
    

min_val = float("inf")

for i in A:
    j = find_from_B(i)
    k1 = find_from_C(i)
    k2 = find_from_C(j)
    min_val = min(min_val, abs(max(i,j,k1) - min(i,j,k1)), abs(max(i,j,k2) - min(i,j,k2)))

print(min_val)

