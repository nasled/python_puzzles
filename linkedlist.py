
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next


node1 = Node('a')
node2 = Node('b')
node3 = Node('c')

node1.set_next(node2)
node2.set_next(node3)

value_of_third_node = node1.get_next().get_next().get_data()
# print(value_of_third_node)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def fill(self):
        self.add('a')
        self.add('a')
        self.add('a')
        self.add('b')
        self.add('b')
        self.add('c')

    def fill_abcdef(self):
        self.add('a')
        self.add('b')
        self.add('c')
        self.add('d')
        self.add('e')
        self.add('f')

    def fill_fedcba(self):
        self.add('f')
        self.add('e')
        self.add('d')
        self.add('c')
        self.add('b')
        self.add('a')

    def first(self):
        return self.head

    def second(self):
        return self.first().get_next()

    '''
    O(1) for head
    '''
    def add(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.length = self.length + 1

    def add_multiple(self, data):
        for i in data:
            self.add(i)

    '''
    O(1) for head
    '''
    def delete(self, data):
        node = self.first()

        if (node.get_data() == data):
            self.head = node.get_next()
            return

        while node.get_next():
            if node.get_next().get_data() == data:
                node.set_next(node.get_next().get_next())
                self.length = self.length - 1
                return
            else:
                node = node.get_next()

    def print(self):
        node = self.first()
        while node:
            print(node.get_data())
            node = node.next


# list = LinkedList()
# list.add('a')
# list.add('b')
# list.add('c')
# # list.add('d')
# # list.add('e')
# list.print()
# list.delete('c')
# list.add('e')
# print('-')
# list.print()

# https://www.geeksforgeeks.org/doubly-linked-list/
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = ''