# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
            self.check =[]

    def dfs(self, node):
            if node is None:
                return
            self.dfs(node.left)
            self.check.append(node.val)
            self.dfs(node.right)
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.dfs(root)
        ans = float('inf')
        for i in range(len(self.check)-1):
            diff = self.check[i+1] - self.check[i]
            ans = min(ans, diff)

        return ans
            

        
