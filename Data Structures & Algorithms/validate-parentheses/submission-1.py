class Solution:
    def isValid(self, s: str) -> bool:
        # ( is acceptable, but need to be closed by ) or ne [ starts
        # correct order
        #   so if ) there needs to be opeen at the left ([]), not ([ )
        stack = []
        brackets = {')': '(', ']' :'[', '}': '{'}
        for b in s:
            if b in brackets:
                # if we find a closing bracket,
                # the past thing in stack has to be same open
                # otherwise fail
                #. If correct clsoing bracket, just remove both from the stack
                # question, how to check for empty list
                if not stack:
                    return False
                if not stack[-1] == brackets[b]: 
                    return False
                stack.pop()
            
            else:
                stack.append(b)

        return not stack
