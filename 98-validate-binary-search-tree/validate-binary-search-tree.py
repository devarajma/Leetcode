# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.check(root)
        for i in range(len(self.res) - 1):
            if self.res[i]>= self.res[i+1]:
                return False
        return True

    def __init__(self):
        self.res = []

    def check(self, root):
        if root is None:
            return
        self.check(root.left)
        self.res.append(root.val)
        self.check(root.right)