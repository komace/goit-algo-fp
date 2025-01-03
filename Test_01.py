
# Задано вузол списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Функція для реверсу списку
def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Функція для вставки нового вузла в відсортований список
def sorted_insert(head, new_node):
    if not head or head.data >= new_node.data:
        new_node.next = head
        return new_node 
    else:
        current = head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return head

# Функція для сортування списку вставкою
def insertion_sort(head):
    sorted_list = None
    current = head
    while current is not None:
        next_node = current.next
        sorted_list = sorted_insert(sorted_list, current)
        current = next_node
    return sorted_list

# Функція для злиття двох відсортованих списків
def merge_lists(head1, head2):
    dummy = Node(0)
    current = dummy
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    current.next = head1 if head1 else head2
    return dummy.next

# Визначення вхідних даних
node1 = Node(11)
node2 = Node(27)
node3 = Node(25)
node1.next = node2
node2.next = node3
node4 = Node(15)
node5 = Node(71)
node6 = Node(35)
node4.next = node5
node5.next = node6

# Перевірка функції reverse_list
reverse_head = reverse_list(node1)
current = reverse_head
print("Результат роботи функції:", end=" ")
while current is not None:
    print(current.data, end=" ")
    current = current.next
print() 

# Перевірка функції insertion_sort
sorted_head = insertion_sort(reverse_head)
current = sorted_head
print("Результат роботи функції:", end=" ")
while current :
    print(current.data, end=" ")
    current = current.next
print()

# Перевірка функції merge_lists
merged_head = merge_lists(sorted_head, node4)
current = merged_head
print("Результат роботи функції:", end=" ")
while current :
    print(current.data, end=" ")
    current = current.next
print()    
