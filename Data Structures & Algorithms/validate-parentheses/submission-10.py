class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        memory = {']':'[', ')':'(', '}':'{'}
        for char in s:
            if char not in memory.keys():
                stk.append(char)
            
            elif stk and stk[-1] == memory[char]:
                stk.pop()
            else:
                return False

        if stk:
            return False
        return True

        
