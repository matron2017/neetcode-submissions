from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #stk where last 2 items we use the notation on
        #, pop thsoe 2 items (poppop)
        #, and 
        stk = []

        for char in tokens:
            if char not in "+-/*":
                stk.append(char)
            else:
                if char == "+":
                    b, a = stk.pop(), stk.pop()
                    stk.append(str(int(a) + int(b)))
                elif char == "-":
                    b, a = stk.pop(), stk.pop()
                    stk.append(str(int(a) - int(b)))
                elif char == "*":
                    b, a = stk.pop(), stk.pop()
                    stk.append(str(int(a) * int(b)))
                elif char == "/":
                    b, a = stk.pop(), stk.pop()
                    div = int(a) / int(b)
                    if div >= 0:
                        stk.append(str(floor(div)))
                    else:
                        stk.append(str(ceil(div)))

        return int(stk[-1])
