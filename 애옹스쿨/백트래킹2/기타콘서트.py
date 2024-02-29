n, m = map(int, input().split())
arr = [input().split() for _ in range(n)]

possible = [0 for i in range(m)]

max_song = 0
guitar = float("inf")
def recur(cur, cnt):
    global max_song, guitar
    if cur == n:
        temp = 0
        for i in range(m):
            if possible[i]:
                temp += 1
        if temp > max_song:
            max_song = temp
            guitar = cnt
        elif temp == max_song:
            guitar = min(guitar, cnt)
        return
    

    # 포함
    songs = arr[cur][1]
    for i in range(m):
        if songs[i] == "Y":
            possible[i] += 1
    
    recur(cur+1, cnt+1)
    for i in range(m):
        if songs[i] == "Y":
            possible[i] -= 1
    

    recur(cur+1, cnt)

recur(0, 0)
if max_song == 0:
    print(-1)
else:
    print(guitar)