import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

even_prefix = [0] * ((n // 2))
odd_prefix = [0] * ((n // 2) - 1)
even_suffix = [0] * ((n // 2))
odd_suffix = [0] * ((n // 2) - 1)

even_prefix[0] = arr[0]
odd_prefix[0] = arr[1]
even_suffix[-1] = arr[-2]
odd_suffix[0] = arr[-3] or 0


print(odd_suffix)


