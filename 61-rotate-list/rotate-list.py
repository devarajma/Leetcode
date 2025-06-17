# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
            
        p = head
        c = 1
        while p.next:
            p = p.next
            c+=1        
        p.next = head

        r = head
        i = 1
        k = k % c
        while i != (c-k):
            r = r.next
            i+=1
        head= r.next
        r.next = None
        return head
