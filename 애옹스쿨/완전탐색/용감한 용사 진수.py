# # 이길 애들을 골라 놓고 이에 맞는 최소 스탯 구하기 -> 100C50 너뮤 큼
# from itertools import combinations as C
# # 결과물은 C(arr, 3) 으로 확인 가능

# n, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# combi = C(arr, k)
# max_stat = float("inf")
# for group in combi:
#     max_str = 0
#     max_dex = 0
#     max_int = 0
#     for i in range(len(group)):
#         max_str = max(max_str, group[i][0])
#         max_dex = max(max_dex, group[i][1])
#         max_int = max(max_int, group[i][2])
    
#     max_stat = min(max_stat, max_str + max_dex + max_int)

# print(max_stat)


# 좌표를 모두 체크해보기 -> 너무 많은 반복문 -> 모든 스탯이 아니라 경계선 스탯만 확인!

n, k = map(int, input().split())

arr = []
str_set = set()
dex_set = set()
inte_set = set()

for _ in range(n):
    str, dex, inte = map(int, input().split())
    arr.append((str, dex, inte))
    str_set.add(str)
    dex_set.add(dex)
    inte_set.add(inte)


min_stat = float("inf")
for str in str_set:
    for dex in dex_set:
        for inte in inte_set:
            cnt = 0
            for s, d, i in arr:
                if s <= str and d <= dex and i <= inte:
                    cnt += 1
            if cnt >= k:
                min_stat = min(min_stat, str + dex + inte)
        
print(min_stat)
# # 색칠해보기??? -> 너무 좌표가 많음
# n, mob = map(int, input().split())
# arr = [[[0] * 1000001 for _ in range(1000001)] for k in range(1000001)]

# for _ in range(n):
#     str, dex, int = map(int, input().split())
#     for i in range(str):
#         for j in range(dex):
#             for k in range(int):
#                 arr[i][j][k] += 1

# for i in range(1000002):
#     for j in range(1000002):
#         for k in range(1000002):
#             if arr[i][j][k] >= mob:
#                 print(i + j + k)
#                 quit() 


