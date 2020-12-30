class Solution:
    def swapPairs_trev(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        s1, s2 = head, head.next
        head = s2
        while s1 and s2:
            nxt1 = s2.next
            nxt2 = s2.next.next if s2.next is not None else None
            s1.next, s2.next = nxt2, s1
            if nxt2 is None: s1.next = nxt1
            s1, s2 = nxt1, nxt2
        return head

s = Solution()
s.swapPairs()