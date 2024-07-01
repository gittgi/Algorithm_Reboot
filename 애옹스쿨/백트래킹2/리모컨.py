n = int(input())
min_val = abs(100 - n)

target = str(n)

ans = ["0" for _ in range(len(target) + 1)]

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



def check():
    num = int("".join(ans[::-1]))
    return abs(n - num)

def recur(cur, cnt):
    global min_val
    if cur >= len(ans)-2 and cur != 0:
        val = check() + cnt
        if val < min_val:
            min_val = val
        if cur == len(ans):
            return
    

    for i in range(10):
        if possible[num_list[i]]:
            if cur < len(ans) - 1:
                ans[cur] = num_list[i]
                recur(cur + 1, cnt + 1)
                ans[cur] = "0"
            
            else:
                if i == 0:
                    ans[cur] = num_list[i]
                    recur(cur + 1, cnt)
                    ans[cur] = "0"
                else:
                    ans[cur] = num_list[i]
                    recur(cur + 1, cnt + 1)
                    ans[cur] = "0"
                    
recur(0, 0)
print(min_val)





