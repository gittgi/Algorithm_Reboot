arr = []
for _ in range(9):
    arr.append(int(input()))

total = sum(arr)
arr.sort()
for i in range(8):
    for j in range(i+1,9):
        if total - arr[i] - arr[j] == 100:
            arr.pop(j)
            arr.pop(i)
            for k in range(7):
                print(arr[k])
            quit()


