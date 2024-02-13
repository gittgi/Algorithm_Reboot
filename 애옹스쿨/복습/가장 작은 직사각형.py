n = int(input())
arr = []
x_list = list()

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
    x_list.append(x)
x_list.sort()
min_val = float("inf")
for x1_idx in range(len(x_list)):
    x1 = x_list[x1_idx]
    for x2_idx in range(x1_idx, len(x_list)):
        x2 = x_list[x2_idx]
        # print(x1, x2)
        # 해당 x 범위에 있는 점들 y 값만 모음
        y_dict = dict()
        for x, y in arr:
            if x1 <= x <= x2:
                y_dict[y] = y_dict.get(y, 0) + 1
        
        y_list = list(y_dict.keys())
        y_list.sort()

        s = 0
        e = 0
        cnt = y_dict[y_list[s]]
        while s <= e:
            
            if cnt >= n // 2:
                # min_val = min(min_val, (2 + y_dict[y_list[e]] - y_dict[y_list[s]]) * (x2 - x1 +2))
                if (2 + y_list[e] - y_list[s]) * (x2 - x1 +2) < min_val:
                    min_val = (2 + y_list[e] - y_list[s]) * (x2 - x1 +2)
                    # print(y_list[e],  y_list[s], x2, x1)
                cnt -= y_dict[y_list[s]]
                s += 1
            else:
                e += 1
                if e >= len(y_list):
                    break
                cnt += y_dict[y_list[e]]
print(min_val)
        

