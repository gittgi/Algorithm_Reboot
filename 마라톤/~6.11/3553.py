n, d = map(int, input().split())

# d로 나눠떨어지는 n자리수

for i in range(10 ** (n-1), 10 ** n):
    if i % d == 0:
        print(i)
        break

else:
    print("No solution")

