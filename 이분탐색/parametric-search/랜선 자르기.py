k, n = map(int, input().split())

wire = [int(input()) for _ in range(k)]

left = 1
right = max(wire)
ans = 0
while left <= right:
    mid = (left + right) // 2
    total = 0
    for i in wire:
        total += (i // mid)

    if total >= n:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(total, ans)
