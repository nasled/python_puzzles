class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_complete_word = False
        self.words_counter = 0

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return Node()

    def getCharCode(self, value):
        return ord(value) - ord('a')

    def add(self, value):
        node = self.root
        for i in range(len(value)):
            charCode = self.getCharCode(value[i])
            if node.children[charCode] is None:
                node.children[charCode] = self.getNode()
            node = node.children[charCode]
            node.words_counter += 1
        node.is_complete_word = True

    def find_count(self, value):
        node = self.root
        result = 0
        for i in range(len(value)):
            charCode = self.getCharCode(value[i])
            if node.children[charCode] is not None:
                node = node.children[charCode]
                result = node.words_counter
            else:
                return 0
        return result

z = Trie()
z.add('hack')
z.add('hackerrank')
print(z.find_count('hac'))
print(z.find_count('hak'))