selected = []
arr = list(map(int, input().split()))
ans = 0

def rec(select):
    global ans
    if len(selected) == 10:
        cnt = 0
        for i in range(10):
            if selected[i] == arr[i]:
                cnt += 1
        if cnt >= 5:
            ans += 1
            print(selected)

        return
    if len(selected) >= 3 and selected[-2] == selected[-1] == select:
        return


    
    selected.append(1)
    rec(1)
    selected.pop()
    selected.append(2)
    rec(2)
    selected.pop()
    selected.append(3)
    rec(3)
    selected.pop()
    selected.append(4)
    rec(4)
    selected.pop()
    selected.append(5)
    rec(5)
    selected.pop()


rec(0)
print(ans)

# for문으로 다시 풀어보기