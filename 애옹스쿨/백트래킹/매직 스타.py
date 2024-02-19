arr = [list(input()) for _ in range(5)]


def check():
    if ans[0] + ans[2] + ans[5] + ans[7] == 26:
        if ans[0] + ans[3] + ans[6] + ans[10] == 26:
            if ans[1] + ans[2] + ans[3] + ans[4] == 26:
                if ans[1] + ans[5] + ans[8] + ans[11] == 26:
                    if ans[4] + ans[6] + ans[9] + ans[11] == 26:
                        if ans[7] + ans[8] + ans[9] + ans[10] == 26:
                            return True
    return False


def recur(cur):

    if cur == 12:
        if check():
            seq = 0
            for i in range(5):
                for j in range(9):
                    if arr[i][j] != ".":
                        arr[i][j] = chr(ans[seq] + 64)
                        seq += 1
            for i in arr:
                print("".join(i))
            quit()
        return
    if fixed[cur]:
        recur(cur + 1)
    else:
        for i in range(1, 13):
            if not visited[i]:
                ans[cur] = i
                visited[i] = True
                recur(cur + 1)
                visited[i] = False


ans = [0 for i in range(12)]
visited = [False for i in range(13)]
fixed = [0 for i in range(12)]

seq = 0
for i in range(5):
    for j in range(9):
        if arr[i][j] == ".":
            continue
        if arr[i][j] != "x":
            ans[seq] = ord(arr[i][j]) - 64
            visited[ord(arr[i][j]) - 64] = True
            fixed[seq] = True
        seq += 1

recur(0)