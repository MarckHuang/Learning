# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solution1
#BFS
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return

        queue = deque([root])
        result = []
        while queue:
            max_val = float("-inf")
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                cur_val = node.val
                max_val = max(max_val, cur_val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max_val)
        return result

#solution2
#DFS
#recursion
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node: TreeNode, curHeight:int) -> None:
            if node is None:
                return
            if curHeight == len(ans):
                ans.append(node.val)
            else:
                ans[curHeight] = max(ans[curHeight], node.val)
            dfs(node.left, curHeight+1)
            dfs(node.right, curHeight+1)
        dfs(root, 0)
        return ans
