#Definition for a binary thee node.
# class TreeNode:
#     def __init__(self, val=0 , left=None, right=None):
#         self.val= val
#         self.left = left
#         self.right = right

#solution1
from collections import deque
class Solution:
    def rightSdieView(self, root:TreeNode):
        if not root:
            return []
        
        queue = deque([root])
        right_view = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):         #遍歷層
                node = queue.popleft()
                # 判斷是否遍歷到單層最後一個元素
                if i == level_size - 1:
                    right_view.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_view
    

#solution2
class Solution:
    def rightSdieView(self, root:TreeNode):
        ans = []

        def dfs(node, level):
            if not node:
                return
            if len(ans) == level:
                ans.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level+1)
        dfs(root,0)
        return ans