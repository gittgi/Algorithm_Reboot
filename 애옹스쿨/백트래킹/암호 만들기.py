l, c = map(int, input().split())

arr = input().split()
arr.sort()
ans = ["" for _ in range(l)]

def recur(cur, start):
    if cur == l:
        if check():
            print("".join(ans))
        return
    
    
    for i in range(start, c):
        ans[cur] = arr[i]
        recur(cur+1, i+1)

def check():
    isVowel = False
    isConst = 0
    for i in ans:
        if i in ["a", "e", "i", "o", "u"]:
            isVowel = True
        else:
            isConst += 1
    
    if isVowel and isConst >= 2:
        return True
    
    return False
        
        
            
                 
    
recur(0,0)