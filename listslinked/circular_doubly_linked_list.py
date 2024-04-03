class Node:
    def __init__(self, data):
        """
        Initialize a new node with given data and next/prev pointers.
        """
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty circular doubly linked list.
        """
        self.head = None

    def create_node(self, data):
        """
        Create a new node with the given data.
        """
        return Node(data)

    def insert_at_beginning(self, data):
        """
        Insert a new node with the given data at the beginning of the linked list.
        """
        new_node = self.create_node(data)
        if not self.head:
            new_node.next = new_node  # Point to itself for circularity
            new_node.prev = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node with the given data at the end of the linked list.
        """
        new_node = self.create_node(data)
        if not self.head:
            new_node.next = new_node  # Point to itself for circularity
            new_node.prev = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node

    def delete_node(self, data):
        """
        Delete the node containing the specified data from the linked list.
        """
        if not self.head:
            print("Error: Linked list is empty")
            return
        current = self.head
        while True:
            if current.data == data:
                if current == self.head:
                    if current.next == self.head:
                        self.head = None
                    else:
                        current.next.prev = current.prev
                        current.prev.next = current.next
                        self.head = current.next
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                del current
                return
            current = current.next
            if current == self.head:
                print("Error: Data not found in the list")
                return

    def search(self, data):
        """
        Search for a node containing the specified data in the linked list.
        """
        if not self.head:
            print("Error: Linked list is empty")
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                return False
                