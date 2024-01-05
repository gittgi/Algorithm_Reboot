n = int(input())

# arr = [0] * (n+1)

for i in range(1, n+1):
    number = i
    for j in str(number):
        number += int(j)

    if number == n:
        print(i)
        break

else:
    print(0)