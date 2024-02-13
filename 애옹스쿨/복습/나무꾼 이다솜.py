n, c, w = map(int, input().split())
arr = []

for _ in range(n):
    tree = int(input())
    arr.append(tree)

max_val = 0

for i in range(1, max(arr)+1):
    chunk = 0
    cut = 0
    for j in range(n):
        tree = arr[j]
        temp_chunk = tree // i
        if tree % i == 0:
            temp_cut = tree // i - 1
        else:
            if tree // i != 0:
                temp_cut = tree // i
        
        if temp_chunk * i * w - temp_cut * c > 0:
            chunk += temp_chunk
            cut += temp_cut
            

    income = chunk * i * w - cut * c
    max_val = max(income, max_val)

print(max_val)

    


