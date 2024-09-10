# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solution1
#recursive
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node == None:
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res


#solution2
#iterable
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return list()
        
        res = list()
        stack = list()
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            #左子樹遍歷完且右子樹為空
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            #有右子樹
            else:
                stack.append(root)
                root = root.right
        
        return res
