class Node:
    def __init__(self, data):
        """
        Initialize a new node with given data and next pointer.
        """
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty circular singly linked list.
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
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node

    def insert_at_end(self, data):
        """
        Insert a new node with the given data at the end of the linked list.
        """
        new_node = self.create_node(data)
        if not self.head:
            new_node.next = new_node  # Point to itself for circularity
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def delete_node(self, data):
        """
        Delete the node containing the specified data from the linked list.
        """
        if not self.head:
            print("Error: Linked list is empty")
            return
        current = self.head
        prev = None
        while True:
            if current.data == data:
                if current == self.head:
                    if current.next == self.head:
                        self.head = None
                    else:
                        prev.next = self.head.next
                        self.head = self.head.next
                else:
                    prev.next = current.next
                del current
                return
            prev = current
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
                