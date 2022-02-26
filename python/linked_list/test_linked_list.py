import pytest
from linked_list import Node, SinglyLinkedList

class TestNode():
    
    def test_init_empty(self):
        empty_node = Node()
        assert empty_node.data is None
        assert empty_node.next is None

    def test_init_not_empty(self):
        node = Node(1)
        assert node.data is 1
        assert node.next is None

