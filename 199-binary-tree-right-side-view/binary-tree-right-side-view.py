# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            
            lvl =[]
            for _ in range(len(q)):
                root = q.popleft()
                lvl.append(root.val)
                if root.left: q.append(root.left)
                if root.right: q.append(root.right)
            res.append(lvl[-1])
        return res

        #     if root.right:
        #         res.append(root.right.val)
        #         if root.left:
        #             q.append(root.left)
        #         q.append(root.right)

        #     elif root.left:
        #         res.append(root.left.val)
        #         q.append(root.left)
                
        # return res


        