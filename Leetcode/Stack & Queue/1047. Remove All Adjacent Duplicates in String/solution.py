
#solution1
#stack
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
    
#solution2
#two pointer
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:

            res[slow] = res[fast]
            #如果和前一位一樣，慢指針就退一步
            if slow > 0 and res[slow] == res[slow-1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return "".join(res[0:slow])