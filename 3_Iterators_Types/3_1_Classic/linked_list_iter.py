from typing import Any, Iterator


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __iter__(self) -> Iterator:
        return LinkedListIterator(self)


class LinkedListIterator:
    def __init__(self, ll: LinkedList) -> None:
        self.current: Node = ll.head

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self.current is not None:
            data = self.current.data
            self.current = self.current.next
            return data
        raise StopIteration