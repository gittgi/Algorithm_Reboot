
a, b = input().split()

a_len = len(a)
b_len = len(b)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n+1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    
    return True

def make_palindrome(n):
    ans = []
    s = int(a)
    e = int(b)
    for i in range(5, 10):
        if s <= i <= e and is_prime(i):
            ans.append(i)

    # 길이가 짝수
    for i in range(1, 10 ** (n//2)):
        num = i
        new_num = str(num) + str(num)[::-1]
        palindrome = int(new_num)
        if s <= palindrome <= e and is_prime(palindrome):
            ans.append(palindrome)
    
    # 길이가 홀수
    for i in range(1, 10 ** (n//2)):
        num = i
        for letter in "0123456789":
            new_num = str(num) + letter + str(num)[::-1]
            palindrome = int(new_num)
            if s <= palindrome <= e and is_prime(palindrome):
                ans.append(palindrome)
    
    ans.sort()
    for i in ans:
        print(i)

    print(-1)


length = len(b)

make_palindrome(length)


