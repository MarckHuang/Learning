# class Node:
#     def __init__(self, val, left, right, next):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

#solution1
#BFS
from collections import deque
class Solution:
    def connet(sefl, root):
        if not root:
            return root
        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev = None

            for i in range(level_size):
                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
    
#solution2
#DFS
class Solution:
    def connect(self, root):
        pre = []
        def dfs(node, depth):
            if node in None:
                return
            if depth == len(pre):          #node是每層最左邊節點
                pre.append(node)
            else:                         
                pre[depth].next = node     #最左邊往右指
                pre[depth] = node
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return root