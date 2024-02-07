import sys
input = sys.stdin.readline

n ,m = map(int,input().split())

arr = list(map(int, input().split()))


s = max(arr)
e = sum(arr)
ans = float("inf")
ans_seq = []
while s <= e:
    mid = (s + e) // 2
    idx = 0
    bag_cnt = 0
    this_bag = 0
    bag_seq = [0]
    ok = True
    while idx <= n-1:
        if this_bag + arr[idx] > mid:
            if this_bag > 0:
                bag_cnt += 1
                bag_seq.append(idx)
                this_bag = 0
            else:
                ok = False
                break
        else:
            this_bag += arr[idx]
            idx += 1
        if m - bag_cnt == n - idx + 1:
            print(bag_cnt, idx)
            for l in range(idx, n-1):
                bag_cnt += 1
                bag_seq.append(l)
   
            break
    
    bag_cnt += 1
    bag_seq.append(idx)

    if not ok:
        s = mid + 1
    else:
        if bag_cnt <= m:
            if ans > mid:
                ans = mid
                ans_seq = bag_seq
            e = mid - 1
        
        else:
            s = mid + 1


print(ans)
print(ans_seq)

