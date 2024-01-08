n = int(input())

# arr = [0] * (n+1)

for i in range(1, n+1):
    number = i
    for j in str(number):
        number += int(j)

    # 계속 number가 바뀌기 때문에 안됨!
    # for j in range(len(str(number))):
    #     number += int(str(number)[j])

    if number == n:
        print(i)
        break

else:
    print(0)