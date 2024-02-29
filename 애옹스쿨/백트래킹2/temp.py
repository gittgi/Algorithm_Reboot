N = int(input())
M = int(input())
ans = abs(N - 100)
if M:
    broken = list(input().split())
    if M == 10:
        print(ans)
    else:

        upper_num = N
        lower_num = N
        while True:
            N_str = list(str(upper_num))
            if not set(N_str) & set(broken):
                break
            else:
                upper_num += 1
                if upper_num > 1000000:
                    break

        while True:
            N_str = list(str(lower_num))
            if not set(N_str) & set(broken):
                break
            else:
                lower_num -= 1
                if lower_num == 0:
                    if '0' in broken:
                        lower_num = -float("inf")
                    break

        upper_ans = upper_num - N + len(str(upper_num))

        lower_ans = N - lower_num + len(str(lower_num))
        print(upper_num, lower_num)
        print(min(upper_ans, lower_ans, ans))

else:
    print(min(ans, len(str(N))))