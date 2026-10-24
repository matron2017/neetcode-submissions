class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        brackets = {'[':']', '{':'}', '(':')'}
        n = len(s)

        for i in range(n):
            
            if s[i] in brackets:
                curr.append(s[i])
            #why not s but curr
            # s = '[]'
            # curr = ['[',]
            #
            elif curr and brackets[curr[-1]] == s[i]:
                curr.pop()

            else:
                return False
        
        if not curr:
            return True
        
        return False
        
            
