# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = []
        l = []
        q.append(root)
        min_v = float('inf')
        while q:
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                l.append(node.val)
                if node.left: 
                    q.append(node.left)
                    # min_v = min(min_v, node.val - node.left.val)
                if node.right: 
                    q.append(node.right)
                    # min_v = min(min_v, node.right.val - node.val)

        l.sort()
        j = 0
        for i in range(1, len(l)):
            min_v = min(min_v, l[i] - l[j])
            j+=1
        return min_v
        