import sys
input = sys.stdin.readline

n = int(input())
arr = input()
E_count = [0] * len(arr)
print(len(arr))
for i in range(len(E_count)):
    if arr[i] == "E":
        E_count[i] = 1

E_suffix = [0] * (len(E_count))

for i in range(len(E_suffix)-2, -1, -1):
    E_suffix[i] = E_suffix[i+1] + E_count[i]

H_count = [0] * len(arr)
for i in range(len(arr)):
    if arr[i] == "H":
        H_count[i] = (2 ** E_suffix[i]) - E_suffix[i] - 1

H_suffix = [0] * len(arr)
for i in range(len(H_suffix)-2, -1, -1):
    H_suffix[i] = H_suffix[i+1] + H_count[i]

ans = 0
for i in range(len(H_suffix)):
    if arr[i] == "W":
        ans += H_suffix[i]

print(ans)