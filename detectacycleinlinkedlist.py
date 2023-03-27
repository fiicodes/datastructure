# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode])  :
        slow=head
        fast=head
        if not head or not head.next:
            return None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if slow!=fast:
            return None


        ptr1=head
        ptr2=slow
        while ptr1!=ptr2:
            ptr1=ptr1.next
            ptr2=ptr2.next
        return ptr1