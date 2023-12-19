# NOTE: Graded 75/100
# WARN: 2nd and 4th tests DO NOT PASS!

import sys

class AVLNode(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def __init__(self):
        self.root = None

    def push(self, value):
        if self.root is None:
            self.root = AVLNode(value)
        else:
            self.root = self._push(self.root, value)

    def _push(self, node, value):
        if node is None:
            return AVLNode(value)
        if value < node.value:
            node.left = self._push(node.left, value)
        else:
            node.right = self._push(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1:
            if value < node.left.value:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if value > node.right.value:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        if y is None:
            return z

        T2 = y.left
        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        if x is None:
            return y

        T2 = x.right
        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def traverse_inorder(self):
        yield from self._traverse_inorder(self.root)

    def _traverse_inorder(self, node):
        if node:
            yield from self._traverse_inorder(node.left)
            yield node.value
            yield from self._traverse_inorder(node.right)

    def traverse_preorder(self):
        yield from self._traverse_preorder(self.root)

    def _traverse_preorder(self, node):
        if node:
            yield node.value
            yield from self._traverse_preorder(node.left)
            yield from self._traverse_preorder(node.right)

    def traverse_postorder(self):
        yield from self._traverse_postorder(self.root)

    def _traverse_postorder(self, node):
        if node:
            yield from self._traverse_postorder(node.left)
            yield from self._traverse_postorder(node.right)
            yield node.value

avl_tree = AVLTree()
for n in map(int, sys.stdin.readline().strip().split(" ")):
    avl_tree.push(n)

print("PREORDER")
print(",".join(map(str, avl_tree.traverse_preorder())) + ",")
print("INORDER")
print(",".join(map(str, avl_tree.traverse_inorder())) + ",")
print("POSTORDER")
print(",".join(map(str, avl_tree.traverse_postorder())) + ",")