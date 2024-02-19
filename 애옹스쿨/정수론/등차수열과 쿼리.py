import sys
input = sys.stdin.readline

def gcd(i, j) :
    if j > i:
        i, j = j, i
    while i % j != 0:
        i, j = j, i % j
    return j

a, d = map(int, input().split())

# prefix_sum = [0] * (1 + 10 ** 6)


# for i in range(1,1 + 10 ** 6):
#     prefix_sum[i] = prefix_sum[i-1] + (a + d*(i-1))
# # print(prefix_sum[:10])

q = int(input())

for _ in range(q):
    instruction, l, r = map(int, input().split())
    if instruction == 1:
        # ans =  prefix_sum[r] - prefix_sum[l-1]
        ans =  a * (r-l+1) + d * ((l+r-2)*(r-l+1)//2)

    else:
        if d == 0:
            ans = a
        elif l == r:
            ans = a + d*(l-1)
        else:
            ans = gcd(a, d)

    print(ans)
    