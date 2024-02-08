from LinkedList import LinkedList
from Node import Node

def merge_lists(left_list: LinkedList | Node, right_list: LinkedList| Node) -> LinkedList | Node:
    left_node = left_list.head if type(left_list) is LinkedList else left_list
    right_node = right_list.head if type(right_list) is LinkedList else right_list
        
    if left_node is None:
        return right_node
    if right_node is None:
        return left_node
    

    if (left_node.data < right_node.data):
        left_node.next = merge_lists(left_node.next, right_node)
        return left_node
    else:
        right_node.next = merge_lists(right_node.next, left_node)
        return right_node