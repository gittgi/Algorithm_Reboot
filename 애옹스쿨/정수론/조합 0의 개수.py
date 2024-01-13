n, m = map(int, input().split())

# cnt_n_2 = 0
# cnt_m_2 = 0
# cnt_n_m_2 = 0



# for i in range(1, n+1):
#     temp = i
#     while temp % 2 == 0:
#         if i <= m:
#             cnt_m_2 += 1

#         if i <= n - m:
#             cnt_n_m_2 += 1

#         cnt_n_2 += 1

#         temp //= 2


cnt_n_5 = 0
cnt_m_5 = 0
cnt_n_m_5 = 0

# 20억번은 너무 많으니 줄여야 한다.
for i in range(1, n+1):
    temp = i
    while temp % 5 == 0:
        if i <= m:
            cnt_m_5 += 1

        if i <= n - m:
            cnt_n_m_5 += 1

        cnt_n_5 += 1

        temp //= 5

print(cnt_n_5 - (cnt_m_5 + cnt_n_m_5))