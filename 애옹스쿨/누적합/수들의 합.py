import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


prefix = [0] * (n+1)

prefix_dict = dict()
prefix_dict[0] = 1

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr1[i-1] - arr2[i-1]

ans = 0
for i in range(1, n+1):
    if prefix[i] in prefix_dict:
       ans += prefix_dict[prefix[i]]
       prefix_dict[prefix[i]] += 1
    else:
        prefix_dict[prefix[i]] = 1

print(ans)
