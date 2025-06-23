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
        if not head or not head.next or k==0:
            return head
        
        length=1
        fast= head
        while fast.next:
            fast = fast.next
            length+=1
        fast.next = head

        slow,i = head,1
        k = length - (k % length)
        print(k)
        while i != k:
            slow = slow.next
            i+=1
        head = slow.next
        slow.next = None
        return head
        