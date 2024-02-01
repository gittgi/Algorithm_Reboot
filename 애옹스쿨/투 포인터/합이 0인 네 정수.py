n =int(input())

A = []
B = []
C = []
D = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

arr1 = []
arr2 = []

for i in range(n):
    for j in range(n):
        arr1.append(A[i] + B[j])
        arr2.append(C[i] + D[j])

arr1.sort()
arr2.sort()
print(len(arr1), len(arr2))

s = 0
e = len(arr2)-1
cnt = 0

while s <= len(arr1) - 1 and e >= 0:
    # print(s, e)
    if arr1[s] + arr2[e] == 0:
        num1 = arr1[s]
        num2 = arr2[e]
        temp_cnt1 = 0
        temp_cnt2 = 0
        # 동점 처리
        while arr1[s] == num1:
            temp_cnt1 += 1
            s += 1
            if s == len(arr1):
                break
        while arr2[e] == num2 :
            temp_cnt2 += 1
            e -= 1
            if e == -1:
                break
        cnt += temp_cnt1 * temp_cnt2
    
    elif arr1[s] + arr2[e] > 0:
        e -= 1
    else:
        s += 1


print(cnt)

