import sys
input = sys.stdin.readline

ota = input().rstrip()
num_list = [0] * len(ota)
for i in range(len(ota)):
    if ota[i] == "(":
        num_list[i] = 1
    else:
        num_list[i] = -1

prefix = [0] * (len(ota) + 1)

for i in range(1, len(prefix)):
    prefix[i] = prefix[i-1] + num_list[i-1]


