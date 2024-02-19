n, k = map(int, input().split())

arr = []
x_set = set()
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
    x_set.add(x)

x_list = list(x_set)
x_list.sort()
min_val = float("inf")
for x_idx1 in range(len(x_list)):
    print("here")
    x1 = x_list[x_idx1]
    for x_idx2 in range(x_idx1, len(x_list)):
        print("here2")
        x2 = x_list[x_idx2]
        y_dict = dict()
        for x, y in arr:
            if x1 <= x <= x2:
                y_dict[y] = y_dict.get(y, 0) + 1
        
        y_list = list(y_dict.keys())
        y_list.sort()
        
        s = 0
        e = 0
        cnt = y_dict[y_list[s]]
        print("here3")
        while s <= e and e < len(y_list):
            print("here4")
            if cnt >= k:
                if min_val > (x2 - x1 + 2) * (y_list[e] - y_list[s] + 2):
                    min_val = (x2 - x1 + 2) * (y_list[e] - y_list[s] + 2)

                cnt -= y_dict[y_list[s]]
                s += 1
            else:
                e += 1
                if e < len(y_list):
                    
                    cnt += y_dict[y_list[e]]
        
print(min_val)
            
        