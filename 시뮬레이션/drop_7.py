import copy

def check():
   pass

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
    print(delete_list)
    