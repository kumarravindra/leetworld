def reverse_linkedlist():
    if not head:
        return prev
        curr = head.next
        head.next = prev
    return self.reverseList(curr, head)

'''
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
'''

'''
 def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
'''