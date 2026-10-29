from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:

            if char in "+-*/":
                if char == "+":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)
                elif char == "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                elif char == "*":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)
                elif char == "/":
                    b, a = stack.pop(), stack.pop()
                    division = a / b
                    if division < 0:
                        stack.append(ceil(division))
                    else:
                        stack.append(floor(division))

            else:
                stack.append(int(char))
        
        return stack[0]