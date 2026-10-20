class MinStack:

    def __init__(self):
        self.stack = []
        self.minum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minum:
            self.minum.append(val)
        else:
            if self.minum[-1] > val:
                self.minum.append(val)
            else:
                self.minum.append(self.minum[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minum[-1]
