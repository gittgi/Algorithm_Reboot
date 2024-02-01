t = int(input())

for _ in range(t):
    k, n = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    arr1 = []
    arr2 = []
    for i in range(n):
        for j in range(n):
            arr1.append(A[i] + B[j])
            arr2.append(C[i] + D[j])
    
    arr1.sort()
    arr2.sort()

    s = 0
    e = len(arr2) - 1
    ans = 0
    diff = float("inf")

    while s <= len(arr1) - 1 and e >= 0:
        flag = False
        weight = arr1[s] + arr2[e]
        if weight == k:
            ans = k
            flag = True
        
        else:
            if abs(k - weight) < diff:
                ans = weight
                diff = abs(k - weight)
            elif abs(k - weight) == diff:
                if weight < ans:
                    ans = weight

        if flag:
            break
        if weight < k:
            s += 1
        else:
            e -= 1
    print(ans)