def find(a):  
    if parents[a] != a:  
        parents[a] = find(parents[a])  
    return parents[a]  

def union(x, y):  
    x = find(x)  
    y = find(y)  
    if x < y:  
        x, y = y, x  
    parents[x] = y  


def robbing():  
    for i in range(1, N+1):  
        if i != parents[i]:  
            continue  
        for j in range(K-1, cnt_friends[i]-1, -1):  
            dp[j] = max(dp[j], dp[j-cnt_friends[i]] + candies[i])  

N, M, K = map(int, input().split())  
candies = [0] + [*map(int, input().split())]  
parents = [i for i in range(N+1)]  
cnt_friends = [1] * (N+1)  

for i in range(M):  
    a, b = map(int, input().split())  
    union(a, b)  

for k in range(1, N+1):  
    if k != parents[k]:  
        root = find(k)  
        candies[root] += candies[k]  
        cnt_friends[root] += cnt_friends[k]  

dp = [0 for _ in range(K)]  
robbing()
print(cnt_friends)
print(max(dp))