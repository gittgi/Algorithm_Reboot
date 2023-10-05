from collections import defaultdict

tc = int(input())
num = {0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}

def dfs(cnt, dd, number):
    global flag
    if flag:
        return
    if cnt == length:
        flag = True
        print(f"Case #{t+1}: {number}")
        return
    
    for i in range(10):
        letter = num[i]
        # 여기서 딕셔너리 복사

        new_dd = dd.copy()
        temp = 0
        for j in letter:
            if new_dd[j] >= 1:
                new_dd[j] -= 1
                temp += 1
            else:
                break
        else:
            dfs(cnt+temp, new_dd, number + str(i))



for t in range(tc):
    dd = defaultdict(int)
    string = input()
    length = len(string)
    for i in string:
        dd.setdefault(i, 0)
        dd[i] += 1
    flag = False
    dfs(0, dd, "")
        

    