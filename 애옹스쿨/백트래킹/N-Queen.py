n = int(input())


visited_y = [False for i in range(n)]

visited_diag_rd = [False for i in range(n * 2 - 1)]

visited_diag_ld = [False for i in range(n * 2 - 1)]

cnt = 0

def recur(cur):
    global cnt
    if cur == n:
        cnt += 1
        return
    

    for i in range(n):
        if not visited_y[i]:
            if not visited_diag_ld[cur + i]:
                if not visited_diag_rd[cur - i + n - 1]:
                    visited_y[i] = True
                    visited_diag_ld[cur + i] = True
                    visited_diag_rd[cur - i + n - 1] = True
                    recur(cur + 1)
                    visited_y[i] = False
                    visited_diag_ld[cur + i] = False
                    visited_diag_rd[cur - i + n - 1] = False

recur(0)

print(cnt)


