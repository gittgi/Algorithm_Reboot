# 방법 1 : 좌표 색칠하기
# n = int(input())

# arr = []
# for _ in range(n):
#     arr.append(tuple(map(int, input().split())))

# ans = 0
# for i in range(n):
#     time = [0] * 1001
#     for j in range(n):
#         if i != j:
#             start = arr[j][0] + 1
#             end = arr[j][1]
#             for t in range(start, end+1):
#                 time[t] = 1
    
#     ans = max(ans, sum(time))
# print(ans)


# 방법 2 : 좌표가 범위 안에 들어가나 확인하기

n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
ans = 0
for i in range(n):
    cnt = 0
    for t in range(1, 1001):
        for j in range(n):
            if i != j:
                start = arr[j][0] + 1
                end = arr[j][1]
                if start <= t <= end:
                    cnt += 1
                    break
    
    ans = max(ans, cnt)
print(ans)