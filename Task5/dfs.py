from Node import Node
from color_converter import rgb_to_hex, hex_to_rgb

def dfs_recursive(node: Node, visited: set=None, color_step: list=None, key: bool=True) -> None:
    if visited is None:
        visited = set()
    
    if node in visited:
        return

    visited.add(node)
    
    if key:
        color_step =  hex_to_rgb(node.color)
    if color_step:
        color_step[0] = color_step[0] + 17
        color_step[1] = color_step[1] + 17 
        color_step[2] = color_step[2] + 17
        node.color = rgb_to_hex(color_step)
    
    if node.left:
        dfs_recursive(node.left, visited, color_step, False)
    if node.right:  
        dfs_recursive(node.right, visited, color_step, False)