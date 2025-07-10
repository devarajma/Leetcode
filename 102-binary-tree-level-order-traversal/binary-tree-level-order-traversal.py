# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        if not root:
            return []

        res = []
        q = deque([root])

        
        while q:   
            sub = [] 
            for _ in range(len(q)):
                root = q.popleft()
                sub.append(root.val)

                if root.left: q.append(root.left)
                if root.right: q.append(root.right)

            res.append(sub)

        return res
        