from typing import Any, Optional


class Node:
    """Класс. Объявляет головной узел списка^"""
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self):
        return f'Node | {self.value}'


class LinkedList:
    """Класс. Работаем с узлами списка"""
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList []'

    def append(self, element: Any) -> None:
        """Функция. Добавляем  узел в список"""
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index) -> None:
        """Функция. Удаляем узел из списка"""

        previous_node = 0
        current_node = self.head
        current_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if current_node is not None:
            if index == 0:
                self.head = current_node.next
                self.length -= 1
                return

        while current_node is not None:
            if current_index == index:
                break
            previous_node = current_node
            current_node = current_node.next
            current_index += 1

        previous_node.next = current_node.next
        self.length -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
my_list.remove(1)
print(my_list)
