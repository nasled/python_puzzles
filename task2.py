from linkedlist import LinkedList
from linkedlist import Node


class Algo21(LinkedList):
    def __init__(self):
        super().__init__()

    def remove_duplicates(self):
        unique = {}
        node = self.first()

        while node:
            if node.get_data() not in unique.keys():
                unique[node.get_data()] = True
                node.set_next(node.get_next().get_next())

            node = node.get_next()

    def remove_duplicates_without_buffer(self):
        node = self.first()

        while node:
            runner = node
            while runner:
                if node.get_data() == runner.get_data():
                    node.set_next(node.get_next().get_next())
                runner = runner.get_next()
            node = node.get_next()


# l = Algo21()
# l.fill()
# l.remove_duplicates()
# l.print()
# l.fill()
# l.remove_duplicates_without_buffer()
# l.print()

class Algo22(LinkedList):
    def __init__(self):
        super().__init__()

    '''
    memory O(n)
    '''
    def find_k_element_from_end(self, node, k):
        if node.get_next() is None:
            return 0
        else:
            index = self.find_k_element_from_end(node.get_next(), k) + 1
            if index == k:
                print(node.get_data())
            return index


    '''
    time O(n), memory O(1)
    '''
    def find_k_element_from_end_2(self, node, k):
        runner = node.get_next()
        current = node.get_next()

        for i in range(k+1):
            runner = runner.get_next()

        while runner:
            current = current.get_next()
            runner = runner.get_next()

        return current.get_data()

# l = Algo22()
# l.fill_fedcba()
# l.find_k_element_from_end(l.first(), 2)
# print(l.find_k_element_from_end_2(l.first(), 2))

class Algo23(LinkedList):
    def __init__(self):
        super().__init__()

    def remove_element(self, node):
        if node.get_next() is None:
            return False

        node.set_next(node.get_next().get_next())
        return True


# l = Algo23()
# l.fill_fedcba()
# l.remove_element(l.first())
# l.print()

# @todo 2.4

def summ25(list1, list2):
    list = LinkedList()
    node1 = list1.first()
    node2 = list2.first()
    stored = 0

    while (node1):
        while (node2):
            result = node1.get_data() + node2.get_data() + stored
            stored = result // 10

            if stored == 1:
                result = result % 10
            list.add(result)

            node2 = node2.get_next()
            node1 = node1.get_next()

    return list

# list1 = LinkedList()
# list1.add(6)
# list1.add(1)
# list1.add(7)
#
# list2 = LinkedList()
# list2.add(2)
# list2.add(9)
# list2.add(5)
#
# list = summ25(list1,list2)
# list.print()

class Algo26(LinkedList):
    def __init__(self):
        super().__init__()

    def get_reverse(self):
        new_list = self.__class__()

        node = self.first()
        while node:
            new_list.add(node.get_data())
            node = node.get_next()

        return new_list

    def is_palindrome(self):
        new_list = self.get_reverse()
        node1 = self.first()
        node2 = new_list.first()

        while node1:
            while node2:
                if node1.get_data() != node2.get_data():
                    return False

                node1 = node1.get_next()
                node2 = node2.get_next()

        return True

# l = Algo26()
# l.add('m')
# l.add('a')
# l.add('d')
# l.add('a')
# l.add('m')
# print(l.is_palindrome())
#
# l = Algo26()
# l.add('m')
# l.add('a')
# l.add('d')
# l.add('a')
# l.add('m1')
# print(l.is_palindrome())


class Algo27(LinkedList):
    def __init__(self):
        super().__init__()

    def set_by_n(self, n):
        node = self.first()

        while node and n > 0:
            n = n-1
            node = node.get_next()

        self.length = self.length - n
        self.head = node

    def last(self):
        node = self.first()
        last = ''

        while node:
            last = node.get_data()
            node = node.get_next()

        return last

    def get_intersection(self, list1, list2):
        # ends of the lists must be the same
        if list1.last() != list2.last():
            return False

        # normalise length
        length = 0;
        if list1.length > list2.length:
            list1.set_by_n(list1.length - list2.length)
            length = list1.length - list2.length
        else:
            list2.set_by_n(list2.length - list1.length)
            length = list2.length - list1.length

        # find intersection
        node1 = list1.first()
        node2 = list2.first()
        counter = 0
        while node1 and node2:
            if node1.get_data() == node2.get_data():
                self.head = node1
                self.length = length - counter
                return self

            node1 = node1.get_next()
            node2 = node2.get_next()
            counter = counter + 1
        return False

# list1 = Algo27()
# list1.add_multiple([1,2,7,9,5,1,3])
# list2 = Algo27()
# list2.add_multiple([1,2,7,6,4])
#
# intersecter = Algo27()
# intersecter.get_intersection(list1,list2).print()


class Algo28(LinkedList):
    def __init__(self):
        super().__init__()

    def last(self):
        node = self.first()

        while node:
            if node.get_next() is None:
                return node
            node = node.get_next()
        return node

    def link_last_to(self, n):
        node = self.first()
        last = self.last()

        while node and n > 0:
            n = n - 1
            node = node.get_next()

        last.set_next(node)

    def get_first_node_of_loop(self):
        slow = self.first()
        fast = self.first()

        while fast.get_next():
            slow = slow.get_next()
            # deep in a loop
            fast = fast.get_next().get_next()

            if slow == fast:
                break

        if not fast.get_next():
            return False

        slow = self.first()
        while slow != fast:
            slow = slow.get_next()
            fast = fast.get_next()

        return fast



# list = Algo28()
# list.add_multiple([9,8,7,6,5,4,3,2,1])
# list.link_last_to(5)
# node = list.get_first_node_of_loop()
# print(node.get_data())



