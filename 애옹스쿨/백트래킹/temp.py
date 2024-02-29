n = int(input())

def check():
    temp = ans[::-1]
    for i in range(1, len(temp)):
        # print(temp[:i], temp[i:2*i])
        if temp[:i] == temp[i:2*i]:
            return False
    
    return True

num = ["1", "2", "3"]
ans = []
def recur(cur):
    if not check():
        # print("here")
        return
    
    if cur == n:
        print("".join(ans))
        quit()
    
    for i in num:
        ans.append(i)
        recur(cur+1)
        ans.pop()


recur(0)