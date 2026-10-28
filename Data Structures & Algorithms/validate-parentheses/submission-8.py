class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        brackets = {')':'(', '}':'{', ']':'['}
        for i in range(n):
            if s[i] not in brackets:
                stack.append(s[i])
            
            elif stack and brackets[s[i]] == stack[-1]:
                stack.pop()

            else:
                return False
        
        if not stack:
            return True
        
        return False
            
            


        
