import sys
input = sys.stdin.readline

t = int(input())

def yaksu(num):
    if num == 0:
        return [0]
    if num == 1:
        return [1]
    
    yaksu_list = []
    for i in range(1, num+1):
        if i * i > num:
            break
        elif i * i == num:
            yaksu_list.append(i)
        else: 
            if num % i == 0:
                yaksu_list.append(i)
                yaksu_list.append(num // i)
    yaksu_list.sort()
    return yaksu_list
    

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    prefix = [0] * (n+1)
    for i in range(1, len(arr)+1):
        prefix[i] = prefix[i - 1] + arr[i-1]
    yaksu_list = yaksu(sum(arr))
   
    for i in yaksu_list:
        idx = 0
        ans = 0
        while idx < len(arr):
            if arr[idx] > i:
                break
            elif arr[idx] == i:
                idx += 1
          
            else:
                step = 1
                flag = True
                while flag:
                    total = prefix[idx + step + 1] - prefix[idx]
                    if total > i:
                        idx += step
                        flag = False
                        break
                    elif total == i:
                        idx += step + 1
                        ans += 1
                      
                        break
                    else:
                        step += 1
                        ans += 1
             
                if not flag:
                    break

        else:
            print(ans)
            # print(i)
            break

            
    
            

        

    