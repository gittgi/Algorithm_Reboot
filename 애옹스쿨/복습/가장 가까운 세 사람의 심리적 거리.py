import sys
input = sys.stdin.readline

t = int(input())

def check(p1, p2):
    cnt = 0
    for i in range(4):
        if p1[i] != p2[i]:
            cnt += 1
    return cnt

for _ in range(t):
    n = int(input())
    arr = list(input().split())
    words = dict()
    for i in arr:
        words[i] = words.get(i, 0) + 1
    ans = 12
    for mbti1 in words:
        words[mbti1] -= 1
        for mbti2 in words:
            if words[mbti2] >= 1:
                words[mbti2] -= 1
                for mbti3 in words:
                    if words[mbti3] >= 1:
                        ans = min(ans, check(mbti1, mbti2) + check(mbti2, mbti3) + check(mbti3, mbti1))
                words[mbti2] += 1
        words[mbti1] += 1
    
    print(ans)



