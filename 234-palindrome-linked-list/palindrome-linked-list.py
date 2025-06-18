# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
            
        f = s = head
        while f and f.next:
            f= f.next.next
            s = s.next
        print(s.val)

        prev = None
        while s:
            temp = s.next
            s.next = prev
            prev = s
            s = temp
        fst = head
        snd = prev

        while snd:
            if fst.val != snd.val:
                return False
            fst = fst.next
            snd = snd.next
            
        return True
        
