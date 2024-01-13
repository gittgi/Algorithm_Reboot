# # 에라토스테네스의 채로 500 까지의 소수를 모두 구하기
# isPrime = [True for i in range(2 * (10 **12) + 1)]
# isPrime[1] = False
# for i in range(2, 2 * (10 **12) + 1):
#     if not isPrime[i]:
#         continue
#     for j in range(i * i, 2 * (10 **12) + 1, i):
#         isPrime[j] = False
# prime = []
# for i in range(1, 2 * (10 **12) + 1):
#     if isPrime[i]:
#         prime.append(i)
# print(len(prime))
# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     # if a > b:
#     #     a, b = b, a
#     target = a + b
#     for i in range(len(prime) - 1):
#         flag = False
#         for j in range(i, len(prime)):
#             if prime[i] + prime[j] == target:
#                 print("YES")
#                 flag = True
#                 break
#         if flag:
#             break
#     else:
#         print("NO")

def prime_check(num):
    if num == 1:
        return False
    
    cnt = 0
    for i in range(2, num+1):
        if i * i > num:
            break
        if num % i == 0:
            cnt += 1
    if cnt == 0:
        return True
    else:
        return False

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(2, a + b // 2):
        if prime_check(i) and prime_check(a + b - i):
            print("YES")
            break
    else:
        print("NO")


        
   
