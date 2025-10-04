class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items += [item]   # manually add instead of using append()

    def pop(self):
        if not self.is_empty():
            popped_item = self.items[-1]
            self.items = self.items[:-1]   # manually remove last item
            return popped_item
        return None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            top = stack.pop()
            if top != pairs[char]:
                return False
        # ignore letters, numbers, and symbols

    return stack.is_empty()


# --- Main program ---
expr = input("Enter an expression with brackets: ")

if is_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")
