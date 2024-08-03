# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#solution1
#define LinkedList length
class Solution(object):
    def length(self,head):
        self.size = 0
        current = head
        while current:
            self.size += 1
            current = current.next

        return self.size
    
    def removeNthFromEnd(self, head, n):
        size =self.length(head)
        remove_idx = self.size - n 
        
        if remove_idx == 0 :
            return head.next
        
        current = head
        start_idx = 0
        #要停在n-1
        while current:
            if start_idx == remove_idx -1:
                current.next = current.next.next
                break
            start_idx += 1
            current = current.next

        return head
            

#solution2
#two pointer
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode(next=head)
        fast = dummy_head
        slow = dummy_head

        #fast to n+1
        for _ in range(n+1):
            fast = fast.next
        #fast move to None
        while fast:
            slow = slow.next
            fast = fast.next
        #delete nth Node
        slow.next = slow.next.next
        return dummy_head.next

        