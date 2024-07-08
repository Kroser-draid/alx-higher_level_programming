#!/usr/bin/python3
"""
Module of linked list
"""


class Node:
    """
    Node Class
    """
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data

        if not isinstance(next_node, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class siglylinkedlist
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        nodes = []
        current = self.__head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            crnt = self.__head
            while crnt.next_node is not None and crnt.next_node.data < value:
                crnt = crnt.next_node
            new_node.next_node = crnt.next_node
            crnt.next_node = new_node
