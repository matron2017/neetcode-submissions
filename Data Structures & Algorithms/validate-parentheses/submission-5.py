
class Solution:
    def isValid(self, s: str) -> bool:
        # [1] .append(2)  - > [1, 2]  ,   pop()  -> [1]
        past = {'{': '}', '[': ']', '(': ')'}
        # ( add
        stack = []
        for bracket in s:
            if bracket in past:
                stack.append(bracket)
            else:
                if not stack or past[stack[-1]] != bracket:
                    return False
                else:
                    stack.pop()
        
        if not stack:
            return True
            
        return False

