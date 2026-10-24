# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        total = 0
        curr = head.next
        
        while curr:
            if curr.val == 0:
                tail.next = ListNode(total)
                total = 0
                tail = tail.next
            else:
                total += curr.val
            curr = curr.next
        return dummy.next
            