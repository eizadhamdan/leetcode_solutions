# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode()
        second = ListNode()
        first = head
        second = head.next
        while second is not None:
            computed_gcd = math.gcd(first.val,second.val)
            gcd_node = ListNode(val=computed_gcd, next=second)
            first.next = gcd_node
            first = first.next.next
            second = second.next
        return head
