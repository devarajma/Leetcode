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
        q = deque()
        q.append(root)
        sub = []
        res = []
        if not root:
            return res
        res = [[root.val]]
        
        while q:    
            for _ in range(len(q)):
                root = q.popleft()

                if root.left:
                    q.append(root.left)
                    sub.append(root.left.val)
                    print(sub)

                if root.right: 
                    q.append(root.right)
                    sub.append(root.right.val)
                    print(sub)

            if sub: 
                res.append(sub)
                print(sub)
                sub =[]
        return res
        