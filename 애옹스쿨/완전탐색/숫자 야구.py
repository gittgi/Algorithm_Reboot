n = int(input())

guess = []

for _ in range(n):
    num, strike, ball = input().split()
    guess.append((num, int(strike), int(ball)))
ans = 0

for i in range(1, 10):
    for j in range(1, 10):
        if i == j: 
            continue
        for k in range(1, 10):
            if i == k or j == k:
                continue

            for num, strike, ball in guess:
                s = 0
                b = 0
                if i == int(num[0]):
                    s += 1
                elif i in (int(num[0]), int(num[1]), int(num[2])):
                    b += 1
                if j == int(num[1]):
                    s += 1
                elif j in (int(num[0]), int(num[1]), int(num[2])):
                    b += 1
                if k == int(num[2]):
                    s += 1
                elif k in (int(num[0]), int(num[1]), int(num[2])):
                    b += 1

                if s != strike or b != ball:
                    break

            else:
                ans += 1

print(ans)