n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# i, j 는 for문으로 고르기
# k, l 은 투포인터로 찾기

min_val = 10 ** 9
for i in range(n - 1):
    for j in range(i + 1, n):
        snowman = arr[i] + arr[j]
        s = 0
        e = len(arr) - 1

        while s < e:
            if s != i and s != j and e != i and e != j:
                if abs(snowman - (arr[s] + arr[e])) < min_val:
                    min_val = abs(snowman - (arr[s] + arr[e]))
                
                if arr[s] + arr[e] < snowman:
                    s += 1
                elif arr[s] + arr[e] > snowman:
                    e -= 1
                else:
                    print(0)
                    quit()
            
            else:
                if s == i or s == j:
                    s += 1
                
                if e == i or e == j:
                    e -= 1

print(min_val)



