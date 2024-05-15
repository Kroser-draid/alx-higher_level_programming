#!/usr/bin/python3
"""class Node

    Raises:
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
"""


class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node. Defaults to None.

        Raises:
            TypeError: is not a Node or None.
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """
        Gets the data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Gets the next node in the linked list.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node, optional): The new next node. Defaults to None.

        Raises:
            TypeError: If the value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList object.
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string containing each node's data on a new line.
        """
        current = self.head
        output = ""
        while current:
            output += str(current.data) + "\n"
            current = current.next_node
        return output.rstrip("\n")

    def sorted_insert(self, value):
        """
         list in sorted order.

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)
        current = self.head
        prev = None

        while current and current.data < value:
            prev = current
            current = current.next_node

        if not prev:
            new_node.next_node = self.head
            self.head = new_node
        else:
            new_node.next_node = current
            prev.next_node = new_node
