# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """


        if not head or not head.next or left == right:
            return head

        cur = head
        count = 1
        prev = None
        st = None

        while cur and count <= right:
            if count < left:
                st = cur
                cur = cur.next
            elif count == left:
                sl = cur
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            else:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            count+=1
        if st:
            st.next = prev
        else:
            head = prev
        sl.next = cur
        return head