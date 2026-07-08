class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int):
        self._stack.append(val)

        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self):
        if self._stack:
            val = self._stack.pop()
            if val == self._min_stack[-1]:
                self._min_stack.pop()

    def top(self):
        if len(self._stack) == 0:
            raise IndexError("Stack is empty")
        else:
            return self._stack[-1]

    def getMin(self):
        if len(self._stack) == 0:
            raise IndexError("Stack is empty")
        else:
            return self._min_stack[-1]


s1 = MinStack()
output = [None]

s1.push(1)
output.append(None)
s1.push(2)
output.append(None)
s1.push(0)
output.append(None)

output.append(s1.getMin())
s1.pop()
output.append(None)
output.append(s1.top())
output.append(s1.getMin())
