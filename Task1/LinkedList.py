from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print('Попереднього вузла не існує')
            return 
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_before(self, current_node: Node, data):
        if current_node is None:
            print('Вузла не існує')
            return 
        
        current = self.head
        prev_node = None
        if current == current_node:
            new_node = Node(data)
            new_node.next = current
            self.head = new_node
            return
        
        while current:
            if current.next == current_node:
                prev_node = current
                break
            current = current.next
            
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev_node = None
        while current and current.data != key:
            prev_node = current
            current = current.next
        if current is None:
            return
        prev_node.next = current.next
        current = None

    def search_element(self, data: int) -> Node | None:
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def reverse_list(self):
        current = self.head
        prev_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node
        return self

    def __get_middle_element(self, node: Node) -> Node:
        if node == None:
            return node
        
        slow = node
        fast = node
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def __sortedMerge(self, left, right):
        result = None
        
        if not left:
            return right
        if not right:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self.__sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.__sortedMerge(left, right.next)
        return result

    def MergeSort(self, node: Node=None):
        if node is None:
            node = self.head
        if node is None or node.next is None:
            return node

        middle = self.__get_middle_element(node)
        next_middle = middle.next
        
        middle.next = None
        
        left = self.MergeSort(node)
        right = self.MergeSort(next_middle)
        
        sorted_list = self.__sortedMerge(left, right)
        return sorted_list