from collections import deque

class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

# Вставка нового значения в дерево
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

# Рекурсивный метод для вставки
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)

# Поиск значения в дереве
    def search(self, value):
        return self._search_recursive(self.root, value)

# Рекурсивный метод для поиска
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


# Обход бинарного дерева в ширину (BFS)
def bfs_traversal(tree):
    if not tree.root:
        return []

    result = []
    queue = deque([tree.root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return result


# Пример использования
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Обход
print(bfs_traversal(tree))