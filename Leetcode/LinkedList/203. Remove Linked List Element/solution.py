# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#solution1
#used current_node.next判斷
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head != None and head.val == val:
            head = head.next

        cur_node = head
        
        #cur_node != None 是為了 當linkedlist內的值都等於val
        while cur_node!= None and cur_node.next != None:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next

        return head
    
#solution2
#used dummy head
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)

        cur_node = dummy_head
        while cur_node.next != None:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
            
        return dummy_head.next