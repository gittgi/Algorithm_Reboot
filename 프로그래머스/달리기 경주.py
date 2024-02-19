def solution(players, callings):
    rank = dict()
    for i in range(len(players)):
        rank[players[i]] = i
    
    for name in callings:
        current_rank = rank[name]
        front_man = players[current_rank-1]
        rank[name] -= 1
        rank[front_man] += 1
        players[rank[name]] = name
        players[rank[front_man]] = front_man
    
  # 핵심은, for문으로 계속 인덱스를 찾으려하지 말고, 인덱스는 딕셔너리로 따로 관리할 것
    

    
    return players