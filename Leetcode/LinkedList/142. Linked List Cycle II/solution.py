# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#solution1
#two pointer
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            #如果有相交點，兩指針必會相等
            if slow == fast:
                #其中一指針返回head，另一指針從相交點開始
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        # If there is no cycle, return None
        return None




#solution2 
#hash table
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visit = set()
        
        while head:
            if head in visit:
                return head
            visit.add(head)
            head = head.next
        return None
        