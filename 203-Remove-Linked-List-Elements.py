class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head  = head.next
        temp = head
        while temp:
            if temp.next and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
