n = int(input())
min_val = abs(100 - n)

target = str(n)
m = int(input())
if m == 0:
    arr = []
else:
    arr = list(input().split())
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
possible = dict()
for i in num_list:
    possible[i] = True

for i in arr:
    possible[i] = False 

channel = ["" for _ in range(len(target) + 1)]

def recur(cur):
    global min_val
    temp = "".join(channel[::-1])
    val = abs(int(temp) - n) + len(str(int(temp)))

    if val < min_val:
        min_val = val

    if cur == len(target)+1:
        return
        
    

    for i in num_list:
        if possible[i]:
            channel[cur] = i
            recur(cur + 1)
            channel[cur] = ""

recur(0)
print(min_val)



