n, m = map(int, input().split())


cnt_n_2 = 0
cnt_m_2 = 0
cnt_n_m_2 = 0

for i in range(1, 2000000001):
    if 2 ** i > n:
        break
    cnt_n_2 += (n // (2 ** i))
    if 2 ** i <= m:
        cnt_m_2 += (m // (2 ** i))
    if 2 ** i <= (n - m):
        cnt_n_m_2 += ((n - m) // (2 ** i))

cnt_n_5 = 0
cnt_m_5 = 0
cnt_n_m_5 = 0

for i in range(1, 2000000001):
    if 5 ** i > n:
        break
    cnt_n_5 += (n // (5 ** i))
    if 5 ** i <= m:
        cnt_m_5 += (m // (5 ** i))
    if 5 ** i <= (n - m):
        cnt_n_m_5 += ((n - m) // (5 ** i))

cnt_2 = cnt_n_2 - cnt_m_2 - cnt_n_m_2
cnt_5 = cnt_n_5 - cnt_m_5 - cnt_n_m_5

print(min(cnt_2, cnt_5))