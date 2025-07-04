# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        f=head
        c = set()
        while f:
            if f in c:
                return f
            else:
                c.add(f)
                f=f.next
        return None
        