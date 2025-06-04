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

#  Прямой обход (Preorder Traversal)
def preorder_traversal(tree):
    result = []
    _preorder_helper(tree.root, result)
    return result

def _preorder_helper(node, result):
    if node:
        result.append(node.value)
        _preorder_helper(node.left, result)
        _preorder_helper(node.right, result)

# Симметричный обход (Inorder Traversal)
def inorder_traversal(tree):
    result = []
    _inorder_helper(tree.root, result)
    return result

def _inorder_helper(node, result):
    if node:
        _inorder_helper(node.left, result)
        result.append(node.value)
        _inorder_helper(node.right, result)

# Обратный обход (Postorder Traversal)
def postorder_traversal(tree):
    result = []
    _postorder_helper(tree.root, result)
    return result

def _postorder_helper(node, result):
    if node:
        _postorder_helper(node.left, result)
        _postorder_helper(node.right, result)
        result.append(node.value)


# Пример использования
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Выполняем обходы
print("Preorder (Прямой):", preorder_traversal(tree))
print("Inorder (Симметричный):", inorder_traversal(tree))
print("Postorder (Обратный):", postorder_traversal(tree))