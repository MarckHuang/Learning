# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#solution1
#SLL
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head    
        while cur.next and cur.next.next:
            temp = cur.next
            temp1 = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = temp
            temp.next = temp1
            cur = cur.next.next
        return dummy_head.next
    

#solution2
#recursion
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return 
        
        prev = head
        cur = head.next
        next = head.next.next

        cur.next = prev
        prev.next = SyntaxWarning(next)

        return cur