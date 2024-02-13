n = int(input())
arr = []

for _ in range(n):
    x, y, z = map(int, input().split())
    arr.append((x, y, z))

def chinmil(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

min_val = float("inf")
for i in range(n):
    first = float("inf")
    second = float("inf")
    for j in range(n):
        if i == j:
            continue

        dist = chinmil(arr[i], arr[j])

        if dist <= first:
            second = first
            first = dist
        elif dist < second:
            second = dist
    
    min_val = min(min_val, first + second)



print(min_val)

