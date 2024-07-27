class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)<= 1:
            return False
        nxt = [0]*len(s)
        self.getNext(nxt, s)
        #len(s) - nxt[-1] = 最小重複子字串
        if nxt[-1]!=0 and len(s)%(len(s)-nxt[-1]) == 0:
            return True

        return False

    def getNext(self, nxt, s):
        j=0
        nxt[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i]!=s[j]:
                j = nxt[j-1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j