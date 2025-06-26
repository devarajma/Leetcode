# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        cur1, cur2 = l1, l2
        carry = 0
        head = ListNode()
        res = head
        while cur1 or cur2:
            n1 = cur1.val if cur1 else 0 
            n2 = cur2.val if cur2 else 0

            ans = n1+n2+carry
            res.next = ListNode((ans % 10)) 
            res = res.next
            carry = ans // 10

            if cur1 : cur1 = cur1.next
            if cur2 : cur2 = cur2.next

        if carry:
            res.next = ListNode(carry) 

        return head.next