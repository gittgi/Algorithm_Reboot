def rec(index):
    if index == n + 1:
        # print(selected)
        ans.append(''.join(map(str, selected)))
        # print(selected)
       
        return
    for i in range(10):
        if visited[i]:
            continue
        if index == 0:
            selected[index] = i
            visited[i] = True
        else:

            if arr[index - 1] == ">":
                if selected[index - 1] > i:
                    selected[index] = i
                    visited[i] = True
                else:
                    continue
            else:
                if selected[index - 1] < i:
                    selected[index] = i
                    visited[i] = True
                else:
                    continue

        rec(index + 1)
        # print(selected)
        selected[index] = False
        visited[i] = False





n = int(input())
arr = list(input().split())
visited = [False] * 10
selected = [False] * (n+1)
ans = []
rec(0)

max_val = max(ans)
min_val = min(ans)

print(max_val)
print(min_val)