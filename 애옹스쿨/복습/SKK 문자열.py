import sys
input = sys.stdin.readline

word = input().rstrip()

prefix = [0] * len(word)
# suffix = [0] * len(word)
s_prefix = [0] * len(word)
# s_suffix = [0] * len(word)

if word[0] == "S":
    prefix[0] = 2
    s_prefix[0] = 1
elif word[0] == "K":
    prefix[0] = -1

# if suffix[-1] == "S":
#     suffix[-1] = 2
#     s_suffix[-1] = 1
# elif suffix[-1] == "K":
#     suffix[-1] = -1


for i in range(1, len(word)):
    if word[i] == "S":
        prefix[i] = prefix[i - 1] + 2
        s_prefix[i] = s_prefix[i - 1] + 1
    elif word[i] == "K":
        prefix[i] = prefix[i - 1] - 1
        s_prefix[i] = s_prefix[i-1]
    else:
        prefix[i] = prefix[i-1]
        s_prefix[i] = s_prefix[i-1]

# for i in range(len(word) - 2, -1, -1):
#     if word[i] == "S":
#         suffix[i] = suffix[i + 1] + 2
#         s_suffix[i] = s_suffix[i+1] + 1
#     elif word[i] == "K":
#         suffix[i] = suffix[i + 1] - 1
#         s_suffix[i] = s_suffix[i+1]
#     else:
#         suffix[i] = suffix[i+1]
#         s_suffix[i] = s_suffix[i+1]
start = -1
end = -1
for i in range(len(word)):
    if prefix[i] == 0:
        if start == -1:
            start = i
        if s_prefix[i] > 0:
            end = i


# for i in range(len(word)):
#     if suffix[i] == 0:
#         if s_suffix[i] > 0:
#             start = i
#             break
print(prefix)
print(s_prefix)
ans = end - start
if ans <= 0:
    print(-1)
else:
    print(ans + 1)

               

