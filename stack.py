
'''
Last In First Out
'''

class EmptyStackException(Exception):
    pass


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        pass


class Stack:
    MAX_INT = 999

    def __init__(self):
        self.top = None
        pass

    def pop(self):
        if self.top is None:
            raise EmptyStackException()
        node = self.top
        self.top = node.next
        return node.data

    def push(self, data):
        stack_node = StackNode(data)
        stack_node.next = self.top
        self.top = stack_node
        pass

    def peek(self):
        if self.top is None:
            raise EmptyStackException()
        return self.top.data

    def is_empty(self):
        return True if self.top is None else False

# stack = Stack()
# stack.push('a')
# stack.push('b')
# stack.push('c')
# stack.push('d')
# print(stack.is_empty())
# print(stack.peek())
# print(stack.pop())
# print(stack.peek())


