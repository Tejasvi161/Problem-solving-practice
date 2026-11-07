class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()

            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


s = MinStack()

s.push(5)
s.push(2)
s.push(8)
s.push(1)

print("Top element:", s.top())
print("Minimum element:", s.getMin())

s.pop()

print("Minimum after pop:", s.getMin())