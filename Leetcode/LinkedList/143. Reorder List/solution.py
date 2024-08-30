# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#solution1
#反轉鏈表
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        #reverse the second part of the list
        pre = None
        cur = mid
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        #merge the two sorted lists
        first, second = head, pre
        while second.next:
            nxt1 = first.next
            nxt2 = second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
        

#solution2
#deque
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        d = deque()
        temp = head
        #除了首元素外，其餘全都加入deque
        while temp.next:
            d.append(temp.next)
            temp = temp.next
        temp = head
        #一後一前加入鏈表
        while len(d):
            temp.next = d.pop()
            temp = temp.next
            if len(d):
                temp.next = d.popleft()
                temp = temp.next
        temp.next = None
