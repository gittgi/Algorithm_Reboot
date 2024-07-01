n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x : (x[1], x[0]))

cnt = 1
end_time = arr[0][1]
idx = 1
while idx < n:
    if end_time <= arr[idx][0]:
        end_time = arr[idx][1]
        cnt += 1
    
    idx += 1

print(cnt)

'''
3
4 4
3 4
2 4

-> 2
'''