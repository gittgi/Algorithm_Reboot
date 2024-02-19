n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr += [1]

# 홀수의 갯수와 짝수의 갯수를 센다.
# e는 뒤로 돌아가지 않는다.
odd = 0
even = 0
max_even = 0

s = 0
e = 0
if arr[s] % 2 == 0:
  even += 1
else:
  odd += 1




while e < n:

    if odd > k:
        if arr[s] % 2 == 0:
          even -= 1
        else:
          odd -= 1
        s += 1
        continue
    else:
        e += 1
        if arr[e] % 2 == 0:
            even += 1
        else:
            odd += 1
        if even > max_even:
            max_even = even
         
print(max_even)