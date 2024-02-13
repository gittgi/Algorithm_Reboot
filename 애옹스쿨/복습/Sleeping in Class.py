import sys
input = sys.stdin.readline

def find(x):
    result = []
    for i in range(1, x+1):
        if i * i == x:
            result.append(i)
            break
        elif i * i > x:
            break
        else:
            if x % i == 0:
                result.append(i)
                result.append(x//i)
    result.sort()
    return result
    


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    yak = find(total)

    prefix = [0] * (n+1)
    pre_set = set()
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + arr[i-1]
        pre_set.add(prefix[i])

    for div in yak:
        for i in range(div, total+1, div):
            if i not in pre_set:
                break
        else:
  
            print( n - (total // div))
            break
    
    else:
        print(0)
    


        
        
