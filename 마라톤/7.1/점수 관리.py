n = int(input())

arr = []

for i in range(n):
    data = input()
    arr.append(data)

for i in range(n):
    arr[i] = arr[i].replace("[", "")
    arr[i] = arr[i].replace("]", "")
    arr[i] = arr[i].replace("\"", "")
    arr[i] = arr[i].replace("{", "")
    arr[i] = arr[i].replace("}", "")
    arr[i] = arr[i].split(",")
    temp = []
    for j in range(3):
        key = arr[i][j].split(":")[0]
        value = arr[i][j].split(":")[1]
        temp.append(value)
    
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    arr[i] = temp
    

        

arr.sort(key=lambda x: x[0])
arr.sort(reverse=True, key=lambda x : x[1])

now = 0
same = 0
now_point = 0
for i in arr:
    point = i[1]
    if point == now_point:
        i.append(now)
        same += 1
    else:
        now = now + 1 + same
        i.append(now)
        same = 0
        now_point = point



for i in arr:
    if i[2] == 0:
        print(i[3], i[0], i[1])