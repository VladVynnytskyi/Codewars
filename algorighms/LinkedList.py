class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end = '->')
            current = current.next
        print('None')

ll = LinkedList()

ll.append(3)
ll.append(54)
ll.append(34)
ll.append(65)
#for n in ll:

ll.display()


































# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
        
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

    
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end= '-')
#             current= current.next
#         print('None')

    # def delete(self, key):
    #         """Видаляє перший вузол зі значенням key"""
    #         current = self.head

    #         # випадок 1: якщо треба видалити голову
    #         if current and current.data == key:
    #             self.head = current.next
    #             return

    #         # випадок 2: шукаємо елемент у середині
    #         prev = None
    #         while current and current.data != key:
    #             prev = current
    #             current = current.next

    #         # якщо не знайшли
    #         if current is None:
    #             return

    #         # переприсвоюємо посилання: prev -> current.next
    #         prev.next = current.next