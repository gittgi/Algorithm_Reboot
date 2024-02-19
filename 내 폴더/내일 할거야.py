n = int(input())

binary = 0

for _ in range(n):
    days, due_date = map(int, input().split())

    binary += ((1 << (days)) - 1) << (due_date - days)
   

# print(bin(binary))

cnt = 0

while True:
    cnt += 1
    if binary & (1 << cnt):
        break

print(cnt - 1)