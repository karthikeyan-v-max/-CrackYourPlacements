# Your task is to implement  2 stacks in one array efficiently. You need to implement 4 methods.

# twoStacks : Initialize the data structures and variables to be used to implement  2 stacks in one array.
# push1 : pushes element into first stack.
# push2 : pushes element into second stack.
# pop1 : pops element from first stack and returns the popped element. If first stack is empty, it should return -1.
# pop2 : pops element from second stack and returns the popped element. If second stack is empty, it should return -1.

# Example:
# Input:
# push1(2)
# push1(3)
# push2(4)
# pop1()
# pop2()
# pop2()
# Output:
# 3 4 -1
# Explanation:
# push1(2) the stack1 will be {2}
# push1(3) the stack1 will be {2,3}
# push2(4) the stack2 will be {4}
# pop1()   the poped element will be 3 from stack1 and stack1 will be {2}
# pop2()   the poped element will be 4 from stack2 and now stack2 is empty
# pop2()   the stack2 is now empty hence returned -1.

# --------------------solution---------------------

class TwoStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    # Function to push an integer into stack 1
    def push1(self, x):
        self.s1.append(x)

    # Function to push an integer into stack 2
    def push2(self, x):
        self.s2.append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        if not len(self.s1):
            return -1
        return self.s1.pop()

    # Function to remove an element from top of stack 2
    def pop2(self):
        if not len(self.s2):
            return -1
        return self.s2.pop()