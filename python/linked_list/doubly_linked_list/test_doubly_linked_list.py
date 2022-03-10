import pytest
from doubly_linked_list import Node, DoublyLinkedList

class TestNodeBase:

    @pytest.fixture(autouse = True)
    def node_fixture(self):
        self.empty_node = Node()
        self.node = Node(1, None, None)
        self.second_node = Node(2, None, None)
        self.third_node = Node(3, None, None)

class TestNode(TestNodeBase):

    def test_init_empty(self):
        assert self.empty_node.data == None
        assert self.empty_node.next == None
        assert self.empty_node.prev == None

    def test_init_not_empty(self):
        assert self.node.data == 1
        assert self.node.next == None
        assert self.node.prev == None

    def test_init_not_empty_with_next(self):
        # I can add a node initiation that passes in the first node to assign the second node and then test it that way
        self.node.next = self.second_node
        self.second_node.prev = self.node
        assert self.node.prev == None
        assert self.node.data == 1
        assert self.node.next == self.second_node
        assert self.node.next.data == self.second_node.data
        assert self.second_node.prev == self.node
        assert self.second_node.next == None

class TestDoublyLinkedListBase:

    @pytest.fixture(autouse = True)
    def doubly_linked_list_fixture(self):
        # Create a linked list with a single node
        self.single_node_linked_list = DoublyLinkedList(Node(1, None, None))
        # Create a linked list with two nodes
        self.double_node_linked_list = DoublyLinkedList(Node(1, None, None))
        self.double_node_linked_list.insert_at_end(Node(2, None, None))
        # Create a linked list with three nodes
        self.triple_node_linked_list = DoublyLinkedList(Node(1, None, None))
        self.triple_node_linked_list.insert_at_end(Node(2, None, None))
        self.triple_node_linked_list.insert_at_end(Node(3, None, None))

class TestDoublyLinkedList(TestDoublyLinkedListBase):

    def test_init_empty(self):
        # Create a linked list with no nodes
        self.empty_linked_list = DoublyLinkedList()
        assert self.empty_linked_list.head == None
        assert self.empty_linked_list.tail == None

    def test_init_not_empty(self):
        # Create a linked list with a single node
        node = Node(1, None, None)
        self.single_node_linked_list = DoublyLinkedList(node)
        assert self.single_node_linked_list.head == node
        assert self.single_node_linked_list.head.data == node.data
        assert self.single_node_linked_list.head.next == None
        assert self.single_node_linked_list.head.prev == None
        assert self.single_node_linked_list.tail == node
        assert self.single_node_linked_list.tail.data == node.data
        assert self.single_node_linked_list.tail.next == None
        assert self.single_node_linked_list.tail.prev == None
    
    def test_traverse_print_from_head(self, capsys):
        # Create a linked list with two nodes
        self.double_node_linked_list = DoublyLinkedList(Node(1, None, None))
        self.double_node_linked_list.insert_at_end(Node(2, None, None))
        self.double_node_linked_list.traverse_print_from_head()
        captured = capsys.readouterr()
        assert captured.out == "1\n2\n"


    #def test_traverse_print_from_tail(self):

    ## TODO: Test cases for the use case of an empty, single, double, & triple node linked list

    #def test_insert_beginning(self):

    #def test_insert_end(self):

    #def test_insert_between_two_nodes(self):

    #def test_remove_node(self):
