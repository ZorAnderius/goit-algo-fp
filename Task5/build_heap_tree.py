from Node import Node

def build_heap_tree(data):
    heap = []
    for value in data:
        heap.append(Node(value))
    if len(heap) > 0:
        for i in range(1, len(heap)):
            current = heap[i]
            parent_index = (i - 1) // 2
            parent = heap[parent_index]
            
            if i % 2 == 1:
                parent.left = current
            else:
                parent.right = current
    return heap[0]