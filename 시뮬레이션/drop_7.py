import copy

def check():
    delete_list = []
    for i in range(7):
       for j in range(7):
        #    숫자를 찾는다
           if arr[i][j] != 0:
                # x 방향 찾기
                target = arr[i][j]
                t = 0
                cnt = 0
                while 0 <= i + t < 7 and arr[i + t][j] != 0:
                    t += 1
                    cnt += 1
                t = 0
                while 0 <= i + t < 7 and arr[i + t][j] != 0:
                    t -= 1
                    cnt += 1
                if target == cnt - 1:
                    delete_list.append((i, j))
                    continue

                # y 방향 찾기
                t = 0
                cnt = 0
                while 0 <= j + t < 7 and arr[i][j + t] != 0:
                    t += 1
                    cnt += 1
                t = 0
                while 0 <= j + t < 7 and arr[i][j + t] != 0:
                    t -= 1
                    cnt += 1
                if target == cnt - 1:
                    delete_list.append((i, j))
                    continue

    return delete_list

def delete(delete_list):
    for x, y in delete_list:
        arr[x][y] = 0
    

def move_down():
    new_arr = list(zip(*arr))
  
    for i in range(7):
        temp = ''
        for j in range(7):
            if new_arr[i][j] != 0:
                temp += str(new_arr[i][j])
        
        temp = temp.zfill(7)

        for j in range(7):
            arr[j][i] = int(temp[j])


origin_arr = [list(map(int, input().split())) for _  in range(7)]
num = int(input())

result = []

for j in range(7):
    arr = copy.deepcopy(origin_arr)
    arr[0][j] = num
    move_down()

    delete_list = check()
    while delete_list:
        delete(delete_list)
        move_down()
        delete_list = check()

    cnt = 0

   
    for l in range(7):
        for k in range(7):
            if arr[l][k] != 0:
                cnt += 1
    result.append(cnt)



print(min(result))     
    