from collections import deque

from color_converter import rgb_to_hex, hex_to_rgb

def bfs_recursive(queue: deque, visited: set=None, color_step: list=None, key: bool=True) -> None:
    if visited is None:
        visited = set()

    if not queue:
        return
    node = queue.popleft()
    if node not in visited:
        if key:
            color_step =  hex_to_rgb(node.color)
            key = False
        if color_step:
            color_step[0] = color_step[0] + 17
            color_step[1] = color_step[1] + 17 
            color_step[2] = color_step[2] + 17
            node.color = rgb_to_hex(color_step)
        
        if node.left and node.left not in visited:
            queue.append(node.left)
            
        if node.right and node.right not in visited:
            queue.append(node.right)
            
        bfs_recursive(queue, visited, color_step, False)