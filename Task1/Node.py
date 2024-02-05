class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def print_nodes(self):
        if self is None:
            print(' ')
            return
        curr_node = self
        while curr_node:
            print(curr_node.data, end = " ")
            curr_node = curr_node.next
        print(' ')