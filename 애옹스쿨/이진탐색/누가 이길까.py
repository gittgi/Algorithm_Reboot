import sys
input = sys.stdin.readline

n, m = map(int, input().split())

hi = list(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()


def binary_search(target):
    s = 0
    e = len(arr) - 1
    l = -1
    while s <= e:
        mid = (s + e) // 2
        
        if arr[mid] == target:
            l = mid
            e = mid - 1
        elif arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    
    if l == -1:
        l = max(s, e)

    s = 0
    e = len(arr) - 1
    u = len(arr)
    while s <= e:
        mid = (s+e) // 2
        if arr[mid] == target:
            u = mid + 1
            s = mid + 1
        elif arr[mid] < target:
            s = mid + 1
        else:
            u = mid
            e = mid - 1
    
    win = l
    draw = u - l
    lose = len(arr) - win - draw
    return (win, draw, lose)

hi_win = 0
arc_win = 0
total_draw = 0

for i in hi:
    win, draw, lose = binary_search(i)
    hi_win += win
    arc_win += lose
    total_draw += draw


print(hi_win, arc_win, total_draw)


