# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solution1
#recursive
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
        #先排出空節點情況
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        #排除值不相同情況
        elif left.val != right.val: return False

        #左右不為空，且值相同
        #此時才遞迴
        outside = self.compare(left.left, right.right) #左子樹:左 、右子樹:右
        inside = self.compare(left.right, right.left) #左子樹:右、右子樹:左
        isSame = outside and inside #左子樹:中、右子樹:中
        return isSame
    
#solution2
#iterative, deuqe
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode: #左右都為空代表對稱
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left)
            queue.append(rightNode.right)
            queue.append(leftNode.right)
            queue.append(rightNode.left)
        return True

#solution3
#iterative, stack
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        st = []
        st.append(roor.left)
        st.append(root.right)
        while st:
            rightNode = st.pop()
            leftNode = st.pop()
            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            st.append(leftNode.left)
            st.append(rightNode.right)
            st.append(leftNode.right)
            st.append(rightNode.left)
        return True
    
#solution4
#BFS
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root.left, root.right])

        while queue:
            level_size = len(queue)
            if level_size % 2 != 0:
                return False
            
            level_vals = []
            for i in range(level_size):
                node = queue.popleft()
                if node:
                    level_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_vals.append(None)

            if level_vals != level_vals[::-1]:
                return False
        return True
