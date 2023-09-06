import sys
import heapq
input = sys.stdin.readline

n, k =map(int, input().split())

gems = [list(map(int, input().split())) for _ in range(n)]

bags = [int(input()) for _ in range(k)]

gems.sort()
bags.sort()
stolen = []
total = 0

for bag in bags: # 작은 가방부터 시작
    
    while gems and gems[0][0] <= bag: # 현재 가방이 들 수 있는 무게인 보석
        gem = heapq.heappop(gems)
        heapq.heappush(stolen, -gem[1]) # 훔칠 수 있는 목록에 추가
    
    if stolen:
        total -= heapq.heappop(stolen) # 현재 훔칠 수 있는 목록 중에서 가장 비싼 것을 현재 가방에 담고 다음 가방 판단


# 결과적으로 작은 가방이 훔칠 수 있는 것들은 큰 가방도 훔칠 수 있기 때문에 작은 가방이 훔칠 수 있는 최대 가치를 먼저 담는 것이 중요

print(total)

