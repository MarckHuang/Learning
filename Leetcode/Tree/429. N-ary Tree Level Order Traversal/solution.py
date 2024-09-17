"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
#solution1
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            levels = []
            for i in range(level_size):
                node = queue.popleft()
                levels.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(levels)
        return result
    
#solution2
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        def traversal(root, depth):
            if len(result) == depth:
                result.append([])
            result[depth].append(root.val)
            if root.children:
                for i in range(len(root.children)):
                    traversal(root.children[i], depth+1)
        traversal(root, 0)
        return result
    
#solution3
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue, res = [root], []
        while queue and queue[0]:
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return res

