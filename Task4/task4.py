from Node import Node

from build_binary_tree import draw_tree

def task4() -> None:
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.left.left.left = Node(11)
    root.left.left.right = Node(15)
    root.left.right = Node(20)
    root.left.right.left = Node(22)
    root.left.right.right = Node(21)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(2)
    root.right.left.left = Node(11)

    # Відображення дерева
    draw_tree(root)

if __name__ == "__main__":
    task4()