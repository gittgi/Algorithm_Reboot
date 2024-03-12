

def recur(total, start, cnt):

    if total > n:
        return 0
    
    if cnt > 4:
        return 0
    
    if total == n:
        return 1

    temp = 0
    for i in range(start, n+1):
        if i * i > n:
            break
        temp += recur(total + (i * i), i, cnt + 1)
    
    return temp


while True:
    n = int(input())
    if n == 0:
        quit()

    

    print(recur(0, 1, 0))

   

