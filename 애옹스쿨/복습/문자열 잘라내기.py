r, c = map(int, input().split())

arr = []
for i in range(r):
    arr.append(input())
jungbok_list = []
for i in range(r-1, -1, -1):
    if i == r-1:
        word = arr[i]
        jungbok = dict()
        for j in range(c):
            if word[j] in jungbok:
                jungbok[word[j]].append(j)
            else:
                jungbok[word[j]] = [j]
        
        jungbok_list = []
        for j in jungbok:
            if len(jungbok[j]) >= 2:
                jungbok_list.append(jungbok[j])
    
    else:
        word = arr[i]
        new_jungbok_list = []
        for j in jungbok_list:
            jungbok = dict()
            for k in j:
                if word[k] in jungbok:
                    jungbok[word[k]].append(k)
                else:
                    jungbok[word[k]] = [k]
            for k in jungbok:
                if len(jungbok[k]) >= 2:
                    new_jungbok_list.append(jungbok[k])

        jungbok_list = new_jungbok_list
    if len(jungbok_list) == 0:
        print(i)
        break

else:
    print(0)