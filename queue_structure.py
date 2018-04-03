
'''
First In First Out
'''

class EmptyQueueException(Exception):
    pass

'''
    (first) 0 <- 1 <- 2 <- 3 (last)
'''
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        pass


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        pass

    '''
    add item at the end of the list
        also save at the first is empty
    '''
    def add(self, data):
        queue_node = QueueNode(data)

        if self.last is not None:
            self.last.next = queue_node

        self.last = queue_node

        if self.first is None:
            self.first = self.last

    '''
    remove first item in the list
    '''
    def remove(self):
        if self.first is None:
            raise EmptyQueueException()

        first = self.first
        self.first = first.next

    '''
    return the first of the list
    '''
    def peek(self):
        if self.first is None:
            raise EmptyQueueException()
        return self.first.data

    def is_empty(self):
        return True if self.last is None else False

# queue = Queue()
# queue.add('a')
# queue.add('b')
# queue.add('c')
# queue.add('d')
# print(queue.is_empty())
# print(queue.peek())
# queue.remove()
# print(queue.peek())
# queue.remove()
# print(queue.peek())
# queue.add('e')
# queue.remove()
# queue.remove()
# print(queue.peek())

