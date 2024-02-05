# Завдання 1. Структури даних. 
# Сортування. Робота з однозв'язним списком

from LinkedList import LinkedList
from merge_lists import merge_lists

def task1() -> None:
    llist = LinkedList()

    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)
    
    element = llist.search_element(25)
    llist.insert_after(element, 7)
    llist.insert_before(element,8)


    print("Однозв'язний список 1:")
    llist.print_list()
 
    print("Відсортований однозв'язний список 1:")
    new_list = llist.MergeSort()
    new_list.print_nodes()
    
    
    llist2 = LinkedList()

    llist2.insert_at_beginning(35)
    llist2.insert_at_beginning(-10)
    llist2.insert_at_beginning(115)
    llist2.insert_at_end(-20)
    llist2.insert_at_end(55)
    
    print("Однозв'язний список 2:")
    llist2.print_list()
    
    print("Реверс одозв'язного списку 2:")
    llist2.reverse_list().print_list()
    
    print("Відсортований однозв'язний список 2:")
    new_list2 = llist2.MergeSort()
    new_list2.print_nodes()
    
    print("Злиття двох відсортованих однозвязних списків:")
    new_list3 = merge_lists(new_list, new_list2)
    new_list3.print_nodes()

if __name__ == "__main__":
    task1()