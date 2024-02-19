n, b, w = map(int, input().split())

road = input()
road += 'W'
s = 0
e = 0
max_len = 0

joyak = {"B":0, "W":0}
joyak[road[0]] += 1

# 한번에 하나만 움직이자..
while e < n:
    if joyak["W"] < w:
        e += 1
        joyak[road[e]] += 1
    elif joyak["B"] > b:
        joyak[road[s]] -= 1
        s += 1
    
    else:
        max_len = max(max_len, e - s + 1)
        e += 1
        joyak[road[e]] += 1

    

print(max_len)