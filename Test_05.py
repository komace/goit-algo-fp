import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Функція для побудови бінарного дерева з масиву
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для відображення бінарного дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Генерація кольорового градієнту
def get_color_gradient(n):
    gradient = []
    for i in range(n):
        value = int(255 * i / n)
        color = f"#{value:02x}{value:02x}ff"
        gradient.append(color)
    return gradient

# обходть дерево в ширину змінюючи кольори вузлів
def bfs(root):
    if not root:
        return []
    queue = deque([root])
    visited = []
    colors = get_color_gradient(len(queue))
    index = 0
    while queue:
        node = queue.popleft()
        node.color = colors[index % len(colors)]
        visited.append(node)
    
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        index += 1
        draw_tree(root)
    return visited        
# обходить дерево в глибину змінюючи кольори вузлів
def dfs(root):
    if root is None:
        return []
    stack = [root]
    visited = []
    colors = get_color_gradient(len(stack))
    index = 0
    while stack:
        node = stack.pop()
        node.color = colors[index % len(colors)]
        visited.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        index += 1
        draw_tree(root)    
    return visited

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("Обхід дерева в ширину:")
bfs(root)
print("Обхід дерева в глибину:")
dfs(root)