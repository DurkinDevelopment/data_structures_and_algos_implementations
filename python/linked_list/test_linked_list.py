import pytest
from linked_list import Node, SinglyLinkedList
class TestNodeBase:
    @pytest.fixture(autouse = True)
    def node_fixture(self):
        self.empty_node = Node()
        self.node = Node(1)
        self.second_node = Node(2)
        self.third_node = Node(3)

class TestNode(TestNodeBase):

    def test_init_empty(self):
        assert self.empty_node.data is None
        assert self.empty_node.next is None

    def test_init_not_empty(self):
        assert self.node.data is 1
        assert self.node.next is None

    def test_init_not_empty_with_next(self):
        self.node.next = self.second_node
        assert self.node.data is 1
        assert self.node.next.data is 2
        assert self.node.next is self.second_node

class TestSinglyLinkedListBase:
    @pytest.fixture(autouse = True)
    def singly_linked_list_fixture(self):
        self.empty_linked_list = SinglyLinkedList()
        self.single_node_linked_list = SinglyLinkedList(Node(1))
        self.double_node_linked_list = SinglyLinkedList(Node(1))
        self.double_node_linked_list.head.next = Node(2)

class TestSinglyLinkedList(TestSinglyLinkedListBase):
    def test_init_empty(self):
        assert self.empty_linked_list.head is None

    def test_init_not_empty(self):
        assert self.single_node_linked_list.head is not None
        assert self.single_node_linked_list.head.data is 1 
        assert self.single_node_linked_list.head.next is None
    
    def test_traverse_print(self, capsys):
        self.double_node_linked_list.traverse_print()
        captured = capsys.readouterr()
        assert captured.out == "1\n2\n"
        

