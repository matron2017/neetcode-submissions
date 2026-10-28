class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        brackets = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char not in brackets:
                stack.append(char)
            
            elif stack and brackets[char] == stack[-1]:
                stack.pop()

            else:
                return False
        
        if not stack:
            return True
        
        return False
            
            


        
