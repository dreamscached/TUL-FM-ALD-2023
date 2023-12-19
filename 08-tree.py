# NOTE: Graded 100/100
# NOTE: All tests pass

import sys

class BiTree(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def push(self, value):
        if self.value is None:
            self.value = value

        elif value < self.value:
            if self.left is None:
                self.left = BiTree(value)
            else:
                self.left.push(value)

        elif value > self.value:
            if self.right is None:
                self.right = BiTree(value)
            else:
                self.right.push(value)

    def traverse(self, strategy):
        yield from strategy(self)

    def __repr__(self):
        return f"BiTree(value={self.value!r} left={self.left!r} right={self.right!r})"

def inorder(tree):
    if tree.left:
        yield from inorder(tree.left)
    yield tree.value
    if tree.right:
        yield from inorder(tree.right)

def preorder(tree):
    yield tree.value
    if tree.left:
        yield from preorder(tree.left)
    if tree.right:
        yield from preorder(tree.right)

def postorder(tree):
    if tree.left:
        yield from postorder(tree.left)
    if tree.right:
        yield from postorder(tree.right)
    yield tree.value


tree = BiTree()
for n in map(int, sys.stdin.readline().strip().split(" ")):
    tree.push(n)

print("preorder")
for n in tree.traverse(preorder):
    print(n)

print("inorder")
for n in tree.traverse(inorder):
    print(n)

print("postorder")
for n in tree.traverse(postorder):
    print(n)