from collections import deque
import heapq

from draw_heap_tree import draw_heap_tree
from build_heap_tree import build_heap_tree
from bfs import bfs_recursive
from dfs import dfs_recursive

def task5() -> None:
    array = [7, 11, -1, 4, 3, 9, 18, 0, 100, 5,-10]
    heapq.heapify(array)

    while True:
        print('\nВиберіть яким алгоритмом ви хочете обійти бінарну купу')
        print('   1 - пошук в ширину (bfs)')
        print('   2 - пошук в глубину (dfs)')
        print('   3 - вихід\n')
        
        input_key = int(input('Введіть номер алгоритму:  '))
        
        if input_key == 3:
            print('Goodbye!')
            break
        
        heap_tree = build_heap_tree(array)
        
        if input_key == 1:
            bfs_recursive(deque([heap_tree]))
            draw_heap_tree(heap_tree)
        
        if input_key == 2:
            dfs_recursive(heap_tree)
            draw_heap_tree(heap_tree)
        else:
            print('Не вірний число виберіть один з трьох варіантів (1, 2, 3)')


if __name__ == "__main__":
    task5()