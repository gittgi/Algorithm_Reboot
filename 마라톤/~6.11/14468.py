arr = input()

# 두번째로 나올때까지 순회하면서, 그 사이에 구번 나온 알파벳은 통과, 한번만 나온 알파벳은 cnt
# 두번씩 세어지기 때문에, 꼭 나누기 2하기
answer = 0
for i in range(len(arr)):
    start = arr[i]
    visited = [0 for i in range(26)]
    for j in range(i+1, len(arr)):
        now = arr[j]
        if now != start:
            visited[ord(now) - ord("A")] += 1
        else:
            answer += visited.count(1)
            break

print(answer // 2)

