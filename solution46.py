class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        dup = -101
        while cur.next:
            if cur.val == cur.next.val:
                dup = cur.val
            if cur.val == dup:
                prev.next = cur.next               
            else:
                prev = prev.next
            cur = cur.next
        if cur.val == dup:
            prev.next = None
        return dummy.next
            