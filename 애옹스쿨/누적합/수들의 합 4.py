import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))


prefix = [0] * (n + 1)

for i in range(1, n+1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

num_dict = dict()
num_dict[0] = 1

cnt = 0
for i in range(1, n+1):
    if prefix[i] - k in num_dict:
        cnt += num_dict[prefix[i] - k]
    
    if prefix[i] in num_dict:
        num_dict[prefix[i]] += 1
    else:
        num_dict[prefix[i]] = 1

# print(prefix, num_dict)
print(cnt)