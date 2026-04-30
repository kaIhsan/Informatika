class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = node(data)
        if self.is_empty():   # diperbaiki
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            removed_data = self.head.data   # indentasi diperbaiki
            self.head = self.head.next
            self.size -= 1
            if self.head is None:
                self.tail = None
            return removed_data

    def peek(self):
        if not self.head:
            return None
        else:
            return self.head.data

    def display(self):
        if self.is_empty():
            return None
        else:
            current = self.head
            values = []
            while current:
                values.append(current.data)
                current = current.next
        return values   