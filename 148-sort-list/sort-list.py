# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        left = head
        mid = self.getMid(head)
        right =mid.next
        mid.next = None


        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left,right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    

    def merge(self, left, right):
        cur  = dum =ListNode(None)
        while left and right:
            if left.val < right.val:
                cur.next = left
                cur =left
                left = left.next
            else:
                cur.next = right 
                cur = right
                right = right.next 
        cur.next = left if left else right
        return dum.next
    