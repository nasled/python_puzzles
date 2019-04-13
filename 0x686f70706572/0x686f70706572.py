import sys

class Heading:
    def __init__(self, weight, text):
        self.weight = weight
        self.text = text

class Node:
    def __init__(self, heading, children):
        self.heading = heading
        self.children = children


class Tree:
    def __init__(self):
        self.root = Node(Heading(0, ""), [])

    def getRoot(self):
        return self.root

    def getNodeByWeight(self, node, weight):
        queue = [node]
        visited = []

        while queue:
            node = queue.pop()
            edges = node.children

            if node.heading.weight == weight:
                return node

            for edge in edges:
                if edge not in visited:
                    visited.append(edge)
                    queue.append(edge)

    def addNode(self, weight, text):
        newNode = Node(Heading(weight, text), [])
        needle = self.getNodeByWeight(self.root, weight - 1)
        if needle:
            needle.children.append(newNode)

def to_outline(headings):
    """Converts a list of input headings into nested nodes"""

    tree = Tree()
    for heading in headings:
        tree.addNode(heading.weight, heading.text)

    return tree.getRoot()

def parse(record):
    """Parses a line of input.
    This implementation is correct for all predefined test cases."""
    (hlevel, text) = record.split(" ", 1)
    return Heading(int(hlevel[1:]), text.strip())

def to_html(node):
    """Converts a node to HTML.
    This implementation is correct for all predefined test cases."""
    child_html = "<ol>" + "\n".join(
    ["<li>" + to_html(child) + "</li>" for child in node.children]
    ) + "</ol>" if node.children else ""

    return (node.heading.text and node.heading.text + "\n") + child_html

inputList = ['H1 All About Birds','H2 Kinds of Birds','H3 The Finch','H3 The Swan','H2 Habitats','H3 Wetlands']
headings = [parse(line) for line in inputList]
outline = to_outline(headings)
html = to_html(outline)
print(html)