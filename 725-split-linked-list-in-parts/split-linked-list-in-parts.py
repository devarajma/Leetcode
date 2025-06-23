# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        # if not head or not head.next:
        #     return []
        length = 0
        fast = head
        while fast:
            fast = fast.next
            length+=1
        
        parts =[]
        part_len = length // k
        extra = length % k
        cur = head

        for i in range(k):
            new = cur
            np = part_len + 1 if extra > 0 else part_len
            extra-=1
            for j in range(np-1):
                if cur:
                    cur = cur.next
            
            if cur:
                newhead = cur.next
                cur.next = None
                cur = newhead
            parts.append(new)

        return parts
        