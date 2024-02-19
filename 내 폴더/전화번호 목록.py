from collections import defaultdict as dict
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, num, is_fin=False ):
        self.num = num
        self.children = {}
        self.is_fin = is_fin

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, num):
        curr_node = self.head

        for i in num:
            if i not in curr_node.children:
                curr_node.children[i] = Node(i)
            
            if curr_node.is_fin:
                return False
            curr_node = curr_node.children[i]
        
        curr_node.is_fin = True
        return True

  
 

    
t = int(input())
for _ in range(t):
    n = int(input())
    num_list = []
    trie = Trie()
    for __ in range(n):
        num = input().strip()
        num_list.append(num)
    
    num_list.sort(key=lambda x: len(x))
    for num in num_list:
        if not trie.insert(num):
            print("NO")
            break
    else:
        print("YES")



    
