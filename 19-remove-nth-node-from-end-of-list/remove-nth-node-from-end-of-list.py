# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def get_size(head):
    cur = head
    c= 0
    while cur:
        c+=1
        cur = cur.next
    return c

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        f=ListNode(0)
        f.next = head
        cur= f
        size = get_size(head)
        for _ in range(size - n ):
            cur = cur.next
        
        cur.next = cur.next.next
        return f.next



        