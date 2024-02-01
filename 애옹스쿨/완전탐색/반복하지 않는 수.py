
arr = [0] * 1000001
idx = 1
number = 0
while idx <= 1000000:
    number += 1
    num = str(number)
    for j in range(len(num)):
        if num[j] in num[j+1:]:
            break
    else:
        arr[idx] = number
        idx += 1

    

    


while True:
    n = int(input())
    if n == 0:
        break
    
  
            
    
    print(arr[n])