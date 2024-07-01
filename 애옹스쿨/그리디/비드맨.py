n = int(input())
arr = []
for i in range(n):
    val = int(input())
    arr.append(val)

max_val = max(arr)
rest_sum = sum(arr) - max_val

# 1. max_val이 나머지 합보다 큰 경우
if max_val > rest_sum:
    print(max_val - rest_sum)

# 2. max_val이 나머지 합이랑 같은 경우
elif max_val == rest_sum:
    print(0)

# 3. max_val이 작은 경우
else:
    
    # 3-1 max_val 과 나머지합의 홀짝이 같음
    if max_val % 2 == rest_sum % 2:
        print(0)
    # 3-2 max_val 과 나머지합의 홀짝이 다름
    else:
        print(1)

