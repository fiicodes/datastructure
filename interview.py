class Solutions:
    def __init__(self,x) :
        self.val=x
        self.next=None
    def hascycle(self,head):
        slow=head
        fast=head
        while fast.next and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False