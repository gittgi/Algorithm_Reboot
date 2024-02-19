# def COD(n):
#     total = 0
#     for i in range(2, n):
#         if i * i > n:
#             break
#         if i * i == n:
#             total += i
#         elif n % i == 0:
#             total += i
#             total += (n // i)
    
#     return total

# num = int(input())

# ans = 0
# for i in range(1, num+1):
#     ans += COD(i)

# print(ans % 1000000)

# 소수인 애들은 합계에 영향을 안줌
# 나머지 애들도 n의 배수인 경우 n을 약수로 가진다
# 따라서 가로로 n의 배수를 세서 n * 갯수로 더해주면 됨


n = int(input())
ans = 0
for i in range(2, int(n**(0.5)) + 1):
    # i의 배수가 몇개인지 구하고 (자기 자신은 세지 않기), 그 개수만큼 곱해서 더하기 -> 가로로 보는 문제!
    ans += (n // i - 1) * i

print(ans % 1000000)