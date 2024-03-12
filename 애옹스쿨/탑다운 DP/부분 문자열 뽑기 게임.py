n = input()

n_lst= list(map(int, list(n)))




# num은 현재 남은 문자열, cur는 player
# return 값은 패자
def recur(cur, lst):

    if list_to_num(lst) == 0:
        return cur % 2
    

    num = list_to_num(lst)
    win = False
    # 내가 이기는 수가 하나라도 있으면 내가 이김
    # 부분 문자열 모두 구하기
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            bu = lst[i:j+1]
            bu_num = list_to_num(bu)
            if bu_num != 0:
                if recur(cur + 1, num_to_list(num - bu_num)) == (cur + 1) % 2:
                    win = True
    
    if win:
        return (cur + 1) % 2
    else:
        return cur % 2


    

def list_to_num(lst):
    temp = 0
    for k in range(len(lst)):
        temp += lst[k] * (10 ** (len(lst) - k -1))
    return temp

def num_to_list(num):
    lst = []
    while num != 0:
        temp = num % 10
        lst.append(temp)
        num //= 10
    return lst[::-1]

ans = 1 << 60
bu_num_list = []
for i in range(len(n)):
    for j in range(i, len(n)):
        bu = n_lst[i:j+1]
        bu_num = list_to_num(bu)
        if bu_num != 0:
            bu_num_list.append(bu_num)


bu_num_list.sort()
print(bu_num_list)
for i in bu_num_list:
    if recur(1, num_to_list(int(n) - i)) == 0:
        print(i)
        break
else:
    print(-1)

print(num_to_list(list_to_num([1, 2, 3, 4])))