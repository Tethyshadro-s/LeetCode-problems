class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        prev = None
        while slow is not None:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        p1 = head
        p2 = prev

        while p2 is not None:
           if p1.val != p2.val:
              return False
           p1 = p1.next
           p2 = p2.next

        return True