import heapq

from draw_heap_tree import draw_heap_tree
from build_heap_tree import build_heap_tree

def task4() -> None:
    array = [7, 11, -1, 4, 3, 9, 18, 0, 100, 5,-10]
    heapq.heapify(array)
    heap_tree = build_heap_tree(array)

    draw_heap_tree(heap_tree)

if __name__ == "__main__":
    task4()