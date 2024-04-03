# Linked Lists Python Module

## Overview

The listslinked Python Module provides implementations for various types of linked lists in Python. Linked lists are fundamental data structures commonly used in computer science and programming.

This module includes implementations for the following types of linked lists:
- Singly Linked List
- Doubly Linked List
- Circular Singly Linked List
- Circular Doubly Linked List

Each type of linked list offers different capabilities and can be used for various applications.

## Installation

You can install the module using pip:

```
pip install listslinked
```

## Usage

To use the linked lists in your Python code, import the desired type of linked list from the module. For example, to use the Singly Linked List:

```python
from listslinked import SinglyLinkedList

# Create a new singly linked list
linked_list = SinglyLinkedList()

# Insert elements
linked_list.insert_at_beginning(5)
linked_list.insert_at_end(10)

# Print the linked list
current = linked_list.get_head()
while current:
    print(current.data)
    current = current.next
```

Similarly, you can use the other types of linked lists provided by the module.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on [GitHub](https://github.com/SpyderRex/linked-lists).

## License

This project is licensed under the MIT License - LICENSE file for details.
