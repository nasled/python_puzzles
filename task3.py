from stack import Stack, StackNode
from linkedlist import LinkedList


class ArraySizeReachedException(Exception):
    pass

class Algo31:
    def __init__(self, max_stack_size = 5, number_of_stacks = 3):
        self.number_of_stacks = number_of_stacks
        self.max_stack_size = max_stack_size
        self.values = [None] * max_stack_size * number_of_stacks
        self.sizes = [0] * number_of_stacks

    def push(self, stack_number, value):
        if self.is_full(stack_number):
            raise ArraySizeReachedException()

        self.sizes[stack_number] = self.sizes[stack_number] + 1
        self.values[self.index_of_top(stack_number)] = value

    def pop(self, stack_number):
        index = self.index_of_top(stack_number)
        value = self.values
        self.values[index] = None
        self.sizes[stack_number] = self.sizes[stack_number] - 1
        return value

    def peek(self, stack_number):
        return self.values[self.index_of_top(stack_number)]

    def is_full(self, stack_number):
        return True if self.max_stack_size == self.sizes[stack_number] else False

    def index_of_top(self, stack_number):
        return stack_number * self.max_stack_size + self.sizes[stack_number] - 1

    def dump(self):
        print(self.sizes)
        print(self.values)
        print('----------')


# q = Algo31(3)
# q.push(1,3)
# q.dump()
# q.push(1,5)
# q.dump()
# q.push(2,3)
# q.dump()
# q.pop(1)
# q.dump()
# print(q.peek(1))
# q.push(2,3)
# q.push(2,3)
# q.dump()



class Algo32MinStackNode:
    def __init__(self, data, minimum):
        self.data = data
        self.min = minimum
        self.next = None


class Algo32asStructure(Stack):
    def __init__(self):
        super().__init__()

    def push(self, data):
        new_min = data if self.min() > data else self.min()

        node = Algo32MinStackNode(data, new_min)
        node.next = self.top
        self.top = node
        return

    def min(self):
        if self.top is None:
            return self.MAX_INT

        return self.top.min

    def pop(self):
        node = self.top
        self.top = node.next

        # looks like a special case in the example
        if node.next is not None:
            return node.next.min

        return node.min


# stack = Algo32asStructure()
# # min 5
# stack.push(5)
# print(stack.min())
# # min 5
# stack.push(6)
# print(stack.min())
# # # min 3
# stack.push(3)
# print(stack.min())
# # # min 3
# stack.push(7)
# print(stack.min())
# # # min 3
# print(stack.pop())
# # # min 5
# print(stack.pop())
# print('---')



class Algo32asAdditionalStack(Stack):
    def __init__(self):
        super().__init__()
        self.mins = Stack()

    def push(self, data):
        if data < self.min():
            self.mins.push(data)
        super().push(data)

    def pop(self):
        value = super().pop()
        if value == self.min():
            self.mins.pop()
        return value

    def min(self):
        if self.mins.top is None:
            return self.mins.MAX_INT

        return self.mins.peek()

    def print(self):
        print(self.min())



# stack = Algo32asAdditionalStack()
# # min 5
# stack.push(5)
# print(stack.min())
# # min 5
# stack.push(6)
# print(stack.min())
# # # min 3
# stack.push(3)
# print(stack.min())
# # # min 3
# stack.push(7)
# print(stack.min())
# # # min 3
# stack.pop()
# print(stack.min())
# # # min 5
# stack.pop()
# print(stack.min())

# stack = Algo32asAdditionalStack()
# stack.push(10)
# stack.push(9)
# stack.push(3)
# stack.push(10)
# stack.push(1)
# stack.pop()
# stack.pop()
# stack.print()



class Algo33SetOfStacks:
    def __init__(self, capacity = 5):
        self.stacks = []
        self.capacity = capacity

    def getLastStack(self):
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[len(self.stacks)-1]

    def push(self, value):
        last = self.getLastStack()

        if last is not None and len(last) < self.capacity:
            last.append(value)
        else:
            stack = []
            stack.append(value)
            self.stacks.append(stack)

    def pop(self):
        last = self.getLastStack()
        elem = last.pop()
        if len(last) == 0:
            self.stacks.pop()
        return elem

    def pop_at(self, stack_number):
        stack = self.stacks[stack_number]
        return_value = stack.pop()

        if len(self.stacks) > stack_number+1:
            self.stacks[stack_number].append(self.stacks[stack_number+1][0])

        # from current stack till the latest
        stack_index = stack_number + 1
        while len(self.stacks) > stack_index:
            # from a head of a stack list to a tail
            for k, i in enumerate(self.stacks[stack_index]):
                # the latest
                if len(self.stacks[stack_index]) == k + 1:
                    # next stack exists
                    if len(self.stacks) > stack_index + 1:
                        if len(self.stacks[stack_index + 1]) == 1:
                            elem = self.stacks[stack_index + 1].pop()
                        # copy the begging of a next stack to latest elem
                        else:
                            elem = self.stacks[stack_index + 1][0]

                        self.stacks[stack_index][self.capacity - 1] = elem
                    else:
                        self.stacks[stack_index].pop()
                elif self.capacity > k + 1:
                    self.stacks[stack_index][k] = self.stacks[stack_index][k + 1]

            stack_index = stack_index + 1
            
        if len(self.getLastStack()) == 0:
            self.stacks.pop()

        return return_value


# stack = Algo33SetOfStacks(3)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.push(6)
# stack.push(7)
# stack.push(8)
# stack.pop()
# print(stack.pop_at(1))
# print(stack.pop_at(1))
# print(stack.stacks)


class EmptyStackException(Exception):
    pass


class Algo34():
    def __init__(self):
        self.newStack = []
        self.oldStack = []

    def add(self, value):
        self.newStack.insert(0, value)
        pass

    def remove(self):
        self.shift()
        return self.oldStack.pop()

    def peek(self):
        self.shift()
        return self.oldStack.pop()

    def is_empty(self):
        return True if len(self.newStack) == 0 else False

    def shift(self):
        if len(self.oldStack) == 0:
            while len(self.newStack) > 0:
                self.oldStack.insert(0, self.newStack.pop())


# queue = Algo34()
# queue.add(1)
# queue.add(2)
# queue.remove()
# queue.remove()
# queue.add(3)
# queue.add(4)
# queue.peek()
# print(queue.peek())'


class Algo35(Stack):
    def __init__(self):
        super().__init__()

    def sort(self):
        result = Stack()
        while self.is_empty() is False:
            tmp = self.pop()
            while result.is_empty() is False and result.peek() > tmp:
                self.push(result.pop())
            result.push(tmp)
        return result

# stack = Algo35()
# stack.push(8)
# stack.push(4)
# stack.push(3)
# stack.push(9)
# stack.push(5)
# stack.push(7)
# sorted = stack.sort()
# while sorted.is_empty() is False:
#     print(sorted.pop())

class EmptyCatsStackException(Exception):
    pass

class EmptyDogsStackException(Exception):
    pass

class Algo36():
    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()

    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.cats.add(animal)

        if isinstance(animal, Dog):
            self.dogs.add(animal)

    def dequeueAny(self):
        if self.dogs.length and self.cats.length:
            cat = self.cats.head.data.date
            dog = self.dogs.head.data.date
            if cat > dog:
                return self.dequeueCat()
            else:
                return self.dequeueDog()

        if self.cats.length:
            return self.dequeueCat()

        if self.dogs.length:
            return self.dequeueDog()

    def dequeueCat(self):
        if self.cats.head is None:
            raise EmptyCatsStackException()

        data = self.cats.head.data
        self.cats.delete(data)
        return data

    def dequeueDog(self):
        if self.dogs.head is None:
            raise EmptyDogsStackException()

        data = self.dogs.head.data
        self.dogs.delete(data)
        return data

class Animal:
    def __init__(self, data, date):
        self.data = data
        self.date = date

    def print(self):
        print(self.data, self.date)

class Dog(Animal):
    def __init__(self, data, date):
        super().__init__(data, date)

class Cat(Animal):
    def __init__(self, data, date):
        super().__init__(data, date)

# shelter = Algo36()
#
# shelter.enqueue(Dog('dog1', 100))
# shelter.enqueue(Dog('dog2', 107))
# shelter.enqueue(Dog('dog2', 102))
# shelter.enqueue(Cat('cat3', 102))
# shelter.enqueue(Cat('cat4', 108))
# shelter.enqueue(Cat('cat5', 103))
# shelter.enqueue(Cat('cat5', 106))
# shelter.enqueue(Cat('cat5', 104))
#
# shelter.dequeueAny().print()
# shelter.dequeueAny().print()
# shelter.dequeueAny().print()
# shelter.dequeueAny().print()
# shelter.dequeueAny().print()
# shelter.dequeueAny().print()
# shelter.dequeueAny().print()
# shelter.dequeueCat().print()
# shelter.dequeueDog().print()
