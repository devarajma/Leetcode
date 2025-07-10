# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque([root])
        res = []
        i = 1

        while q:
            lvl = []
            for _ in range(len(q)):
                root = q.popleft()
                lvl.append(root.val)

                if root.left: q.append(root.left)
                if root.right: q.append(root.right)
                
            res.append(lvl[::i])
            i *= -1



        return res
        