n = int(input())
w, h = map(int, input().split())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[0], x[1]))

def is_there(x, y):

    s = 0
    e = n - 1
    l = -1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid][0] >= x:
            l = mid
            e = mid - 1
        else:
            s = mid + 1

    s = 0
    e = n - 1
    u = -1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid][0] <= x:
            u = mid + 1
            s = mid + 1
        else:

            e = mid - 1

    #TODO: l 조건??? u 조건을 같이 넣어주니까 안됨..
    if l == -1:
        return False
    
    s = l
    e = u-1
    while s <= e:
        mid = (s+e) // 2
        if arr[mid][1] == y:
            # if (x, y) == (6, 3):
                # print("u, l :", u, l, x, y)
            return True
        elif arr[mid][1] > y:
            e = mid - 1
        else:
            s = mid + 1
    # print((x, y), l, u)
    return False
    

    
        


cnt = 0
for x, y in arr:
    if (is_there(x+w, y) and is_there(x, y+h) and is_there(x+w, y+h)):
        # print("answer : ", x, y)
        cnt += 1

print(cnt)