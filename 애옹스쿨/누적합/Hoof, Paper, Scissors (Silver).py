# hoof > scissors > paper > hoof

n = int(input())
arrH = [0] * n
arrS = [0] * n
arrP = [0] * n
for i in range(n):
    letter = input()
    if letter == "H":
        arrH[i] = 1
    elif letter == "S":
        arrS[i] = 1
    else:
        arrP[i] = 1



P_pre = [0] * (n+1)
H_pre = [0] * (n+1)
S_pre = [0] * (n+1)

for i in range(1, n+1):
    P_pre[i] = P_pre[i-1] + arrP[i-1]
    S_pre[i] = S_pre[i-1] + arrS[i-1]
    H_pre[i] = H_pre[i-1] + arrH[i-1]

ans = 0
for i in range(1, n+1):
    P = P_pre[i] + max(S_pre[n] - S_pre[i-1], H_pre[n] - H_pre[i-1])
    H = H_pre[i] + max(S_pre[n] - S_pre[i-1], P_pre[n] - P_pre[i-1])
    S = S_pre[i] + max(P_pre[n] - P_pre[i-1], H_pre[n] - H_pre[i-1])
    ans = max(ans, max(P,S,H))

print(ans)