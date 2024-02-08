class Node:
    def __init__(self, data: int=None) -> None:
        self.data = data
        self.next = None
    
    def print_nodes(self) -> None:
        if self is None:
            print(' ')
            return
        curr_node = self
        while curr_node:
            print(curr_node.data, end = " ")
            curr_node = curr_node.next
        print(' ')