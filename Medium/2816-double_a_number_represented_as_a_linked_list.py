# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Logic:
            if node value is less than 5 simply double it, is=f node value is 
            greater than or equal to 5 double it and add 1.
            edge case- when first node value is greater than 5, double it
            and create a new head with value equal to 1
        """

        new_head = head

        if head.val >= 5:
            new_head = ListNode(1, head)

        node = head
        while node is not None:
            ret = 1 if node.next is not None and node.next.val >= 5 else 0
            node.val = (node.val * 2 + ret) % 10
            node = node.next

        return new_head
    