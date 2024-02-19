import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

numbers = [0] * (max(arr) + 1)
points = [0] * (max(arr) + 1)

for i in range(n):
    numbers[arr[i]] = 1 



for i in range(n):
    num = arr[i]
    k = 2
    while num * k <= max(arr):
        if numbers[num * k] == 1: 
            points[num * k] -= 1
            points[num] += 1
        k += 1
            

 
        
for i in arr:
    print(points[i], end=" ")