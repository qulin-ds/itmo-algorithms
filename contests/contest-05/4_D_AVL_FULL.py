import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.h = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.h

    def update_height(self, node):
        node.h = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

    def balance(self, node):
        return self.height(node.right) - self.height(node.left)

    def rotate_left(self, a):
        b = a.right
        a.right = b.left
        b.left = a

        self.update_height(a)
        self.update_height(b)

        return b

    def rotate_right(self, a):
        b = a.left
        a.left = b.right
        b.right = a

        self.update_height(a)
        self.update_height(b)

        return b

    def rebalance(self, node):
        self.update_height(node)

        b = self.balance(node)

        if b == 2:
            if self.balance(node.right) < 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        if b == -2:
            if self.balance(node.left) > 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        return node

    def _add(self, node, x):
        if node is None:
            return Node(x)

        if x < node.key:
            node.left = self._add(node.left, x)
        elif x > node.key:
            node.right = self._add(node.right, x)
        else:
            return node

        return self.rebalance(node)

    def add(self, x):
        self.root = self._add(self.root, x)

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, node, x):
        if node is None:
            return None

        if x < node.key:
            node.left = self._delete(node.left, x)

        elif x > node.key:
            node.right = self._delete(node.right, x)

        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            minimum = self._find_min(node.right)
            node.key = minimum.key
            node.right = self._delete(node.right, minimum.key)

        return self.rebalance(node)

    def delete(self, x):
        self.root = self._delete(self.root, x)

    def exists(self, x):
        current = self.root

        while current is not None:
            if current.key == x:
                return True

            if x < current.key:
                current = current.left
            else:
                current = current.right

        return False

    def next_key(self, x):
        current = self.root
        answer = None

        while current is not None:
            if current.key >= x:
                answer = current.key
                current = current.left
            else:
                current = current.right

        return answer

    def prev_key(self, x):
        current = self.root
        answer = None

        while current is not None:
            if current.key <= x:
                answer = current.key
                current = current.right
            else:
                current = current.left

        return answer

    def root_key(self):
        if self.root is None:
            return None
        return self.root.key

    def tree_height(self):
        return self.height(self.root)

    def preorder(self):
        if self.root is None:
            return "Empty"

        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(str(node.key))

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return " ".join(result)


def main():
    input = sys.stdin.buffer.readline

    q = int(input())
    tree = AVLTree()
    output = []

    for _ in range(q):
        command = input().split()
        operation = command[0]

        if operation == b"add":
            tree.add(int(command[1]))

        elif operation == b"del":
            tree.delete(int(command[1]))

        elif operation == b"exists":
            x = int(command[1])
            output.append("YES" if tree.exists(x) else "NO")

        elif operation == b"next":
            x = int(command[1])
            answer = tree.next_key(x)
            output.append(str(answer) if answer is not None else "None")

        elif operation == b"prev":
            x = int(command[1])
            answer = tree.prev_key(x)
            output.append(str(answer) if answer is not None else "None")

        elif operation == b"root":
            answer = tree.root_key()
            output.append(str(answer) if answer is not None else "Empty")

        elif operation == b"height":
            output.append(str(tree.tree_height()))

        elif operation == b"print":
            output.append(tree.preorder())

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
