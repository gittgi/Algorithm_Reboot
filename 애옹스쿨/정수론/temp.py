import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

# arr_a를 7로 나눈 나머지에 따라 그룹화
groups = [[] for _ in range(7)]
for num in arr_a:
    groups[num % 7].append(num)

# arr_b를 7로 나눈 나머지에 따라 수행
for i in range(m):
    to_add = arr_b[i] % 7
    new_groups = [[] for _ in range(7)]
    
    for j in range(7):
        if j != to_add:
            new_groups[j] = groups[j][:]

    groups = new_groups[:]

# 결과 출력
result = []
for group in groups:
    result.extend(group)

print(len(result))
print(*result)