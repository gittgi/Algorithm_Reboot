l, c = map(int, input().split())
arr = list(input().split())
arr.sort()

ans = []
vowel = 0
const = 0

def recur(cur):
    global vowel, const
    if vowel + const > l:
        return
    if cur == c:
        if vowel >= 1 and const >= 2 and vowel + const == l:
            print("".join(ans))
        return

    
    

    # 포함
    ans.append(arr[cur])
    if arr[cur] in ['a', 'e', 'i', 'o', 'u']:
        vowel += 1
        recur(cur+1)
        vowel -= 1
    else:
        const += 1
        recur(cur+1)
        const -= 1
    ans.pop()

    # 미포함
    recur(cur + 1)

recur(0)