import sys
input = sys.stdin.readline


arr = input().rstrip()

bracket = dict()
bracket["("] = 1
bracket[")"] = -1
vps = [0] * len(arr)
prefix = [0] * len(arr)
vps[0] = bracket[arr[0]]

suffix = [0] * len(arr)


for i in range(1, len(arr)):
    vps[i] = vps[i-1] + bracket[arr[i]]


prefix[0] = True

if vps[-1] >= 2:
    suffix[-1] = True
else:
    suffix[-1] = False

for i in range(1, len(arr)):
    if prefix[i-1] and vps[i-1] >= 0:
        prefix[i] = True
    else:
        prefix[i] = False

for i in range(len(arr)-2, -1, -1):
    if suffix[i+1] and vps[i] >= 2:
        suffix[i] = True
    else:
        suffix[i] = False
ans = 0
for i in range(len(arr)):
    if arr[i] == "(":
        if vps[-1] == 2 and prefix[i] and suffix[i]:
            ans += 1
    if arr[i] == ")":
        if vps[-1] == -2 and prefix[i]:
            ans += 1


print(vps)
print(prefix)
print(suffix)
print(ans)

