
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#soltuion1
#two pointer      
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head   
        pre = None
        while cur:
            temp = cur.next # 保存一下 cur的下一个節點，因为接下来要改變cur->next，避免斷鍵
            cur.next = pre #反轉
            #更新pre、cur指針
            pre = cur
            cur = temp
        return pre
    
#solution2
#recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)
    
    def reverse(self, cur: ListNode, pre: ListNode)->ListNode:     #cur=head, pre=None
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)     #cur=temp, pre=cur

