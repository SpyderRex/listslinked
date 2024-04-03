class Node:
    def __init__(self, data):
        """
        Initialize a new node with given data and next pointer.
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
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
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node with the given data at the end of the linked list.
        """
        new_node = self.create_node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after_node(self, node, data):
        """
        Insert a new node with the given data after the specified node in the linked list.
        """
        if not node:
            print("Error: Node cannot be None")
            return
        new_node = self.create_node(data)
        new_node.next = node.next
        node.next = new_node

    def delete_node(self, data):
        """
        Delete the node containing the specified data from the linked list.
        """
        current = self.head
        if current and current.data == data:
            self.head = current.next
            del current
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if not current:
            print("Error: Data not found in the list")
            return
        prev.next = current.next
        del current

    def delete_at_beginning(self):
        """
        Delete the first node in the linked list.
        """
        if not self.head:
            print("Error: Linked list is empty")
            return
        temp = self.head
        self.head = self.head.next
        del temp

    def delete_at_end(self):
        """
        Delete the last node in the linked list.
        """
        if not self.head:
            print("Error: Linked list is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_after_node(self, node):
        """
        Delete the node after the specified node in the linked list.
        """
        if not node or not node.next:
            print("Error: Node or next node cannot be None")
            return
        temp = node.next
        node.next = temp.next
        del temp

    def search(self, data):
        """
        Search for a node containing the specified data in the linked list.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def get_length(self):
        """
        Return the number of nodes in the linked list.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        """
        Check if the linked list is empty.
        """
        return self.head is None

    def get_head(self):
        """
        Return a reference to the first node in the linked list.
        """
        return self.head

    def get_tail(self):
        """
        Return a reference to the last node in the linked list.
        """
        current = self.head
        while current and current.next:
            current = current.next
        return current

    def reverse(self):
        """
        Reverse the order of nodes in the linked list.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        """
        Sort the elements of the linked list in ascending order.
        """
        if not self.head:
            return
        sorted_list = []
        current = self.head
        while current:
            sorted_list.append(current.data)
            current = current.next
        sorted_list.sort()
        current = self.head
        for item in sorted_list:
            current.data = item
            current = current.next

    def merge(self, other_linked_list):
        """
        Merge another linked list with the current linked list.
        """
        if not other_linked_list.head:
            return
        tail = self.get_tail()
        tail.next = other_linked_list.head

    def clear(self):
        """
        Remove all nodes from the linked list.
        """
        current = self.head
        while current:
            temp = current.next
            del current
            current = temp
        self.head = None
        