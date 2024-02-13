import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))






even_prefix = [0] * ((n // 2))
odd_prefix = [0] * ((n // 2))





for i in range(n):
    if i % 2 == 0:
        even_prefix[i // 2] = even_prefix[(i // 2) - 1] + arr[i]
    else:
        odd_prefix[i // 2] = odd_prefix[(i // 2) - 1] + arr[i]
        
            
even_prefix = [0] + even_prefix
odd_prefix = [0] + odd_prefix

total = even_prefix[-1]

for i in range(n):
    # 상대 번째에 밑장 빼기

    val = even_prefix[i // 2 + 1] - even_prefix[0] + odd_prefix[n // 2] - odd_prefix[i // 2]
    # print(even_prefix[i // 2] - even_prefix[0], odd_prefix[n // 2 - 1] - odd_prefix[i // 2])
    if val > total:
        print(odd_prefix[n // 2] - odd_prefix[i // 2])
        total = val


print(odd_prefix)
print(even_prefix)
print(total)