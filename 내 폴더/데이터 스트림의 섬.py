from collections import deque

n = int(input())

for tc in range(1, n + 1):
    input_data = list(map(int, input().split()))[1:]

    stack = deque()

    stack.append(input_data[0])

    island = 0

    for i in range(1, len(input_data)):
        num = input_data[i]
        prev = stack.pop()
        if num > prev:
            stack.append(prev)
            stack.append(num)
        elif num == prev:
            stack.append(prev)
        else:
            while num < prev:
                island += 1
                prev = stack.pop()
            
            if num > prev:
                stack.append(prev)
                stack.append(num)
            else:
                stack.append(prev)
    print(' ')
    print('# ', island)