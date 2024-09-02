#solution1
#use stack
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        第一種([{}](): 遍歷完，但stack不為空 => 沒有相對應的左括號來匹配
        第二種([{}}} : 遍歷字符串匹配過程中，stack內沒有要匹配的字符
        第三種([{}]))) : 遍歷字符串匹配過程中，stack已經空，沒有匹配的字符了
        '''
        stack = []

        for item in s:
            if item == "(":
                stack.append(')')
            elif item == "[":
                stack.append("]")
            elif item == "{":
                stack.append("}")
            #第二種與第三種
            elif not stack or stack[-1] != item:
                return False 
            else:
                #匹配到的要popout
                stack.pop()
        #第一種
        return True if not stack else False
    
#solution2
#use dict
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item:
                return False 
            else:
                #匹配到的要popout
                stack.pop()
        #第一種
        return True if not stack else False
    
