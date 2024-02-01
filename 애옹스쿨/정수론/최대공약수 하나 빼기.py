n = int(input())

def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b

arr = [map(int, input().split())]
arr.sort()


        


        
            
            
