n = int(input())
word = input()

s = 0
e = 0
letter_dict = dict()

letter_dict[word[s]] = 1

ans = 1


while e < len(word) - 1:
    e += 1
    if word[e] in letter_dict:
        letter_dict[word[e]] += 1
    else:
        letter_dict[word[e]] = 1
    
    while len(letter_dict) > n:
        letter_dict[word[s]] -= 1
        if letter_dict[word[s]] == 0:
            letter_dict.pop(word[s])
        s += 1
        
    
    ans = max(ans, e - s + 1)

print(ans)

