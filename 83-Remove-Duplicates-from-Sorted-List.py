class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        while temp:
            while temp.next and temp.next.val == temp.val:
                temp.next = temp.next.next
            temp = temp.next
        return head
