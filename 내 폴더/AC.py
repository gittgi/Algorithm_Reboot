import sys
from collections import deque

input = sys.stdin.readline


tc = int(input())

for _ in range(tc):

    command = input().rstrip()
    length = int(input())
    line = input().rstrip()
    q = deque(line[1:len(line)-1].split(','))

    
    rev_cnt = 0 # 뒤집기가 소요가 많이 되기 때문에, 일단 뒤집지 않고 뒤집어야 하는 횟수만 저장
    for i in command:
        if i == "R":
            rev_cnt += 1
        if i == 'D':
            if len(q) == 0 or q[0] == '':
                print("error")
                break
            else:
                if rev_cnt % 2: # 현재 뒤집어야 하는 횟수(상태)에 따라서 앞에서 빼는 것과 뒤에서 빼는 것이 달라짐
                    q.pop()
                else:
                    q.popleft()
    else:
  
        if q:
            if rev_cnt % 2:
                q.reverse()
            print("["+",".join(q)+"]")
      
        else:
            print("[]")