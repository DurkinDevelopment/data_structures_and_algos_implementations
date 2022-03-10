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

class TestDoublyLinkedList():

    def test_init_empty(self):
        # Create a linked list with no nodes
        empty_linked_list = DoublyLinkedList()
        assert empty_linked_list.head == None
        assert empty_linked_list.tail == None

    def test_init_not_empty(self):
        # Create a linked list with a single node
        node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(node)
        assert single_node_linked_list.head == node
        assert single_node_linked_list.head.data == node.data
        assert single_node_linked_list.head.next == None
        assert single_node_linked_list.head.prev == None
        assert single_node_linked_list.tail == node
        assert single_node_linked_list.tail.data == node.data
        assert single_node_linked_list.tail.next == None
        assert single_node_linked_list.tail.prev == None
    
    def test_traverse_print_from_head(self, capsys):
        # Create a linked list with two nodes
        double_node_linked_list = DoublyLinkedList(Node(1, None, None))
        double_node_linked_list.insert_at_end(Node(2, None, None))
        double_node_linked_list.traverse_print_from_head()
        captured = capsys.readouterr()
        assert captured.out == "1\n2\n"


    def test_traverse_print_from_tail(self, capsys):
        # Create a linked list with two nodes
        double_node_linked_list = DoublyLinkedList(Node(1, None, None))
        double_node_linked_list.insert_at_end(Node(2, None, None))
        double_node_linked_list.traverse_print_from_tail()
        captured = capsys.readouterr()
        assert captured.out == "2\n1\n"

    ## TODO: Test cases for the use case of an empty, single, double, & triple node linked list

    def test_insert_at_beginning_empty_to_single(self):
        # Create a linked list with no nodes
        empty_linked_list = DoublyLinkedList()
        assert empty_linked_list.head == None
        assert empty_linked_list.tail == None
        # Create a new node and insert it at the beginning of the empty list
        node = Node(1, None, None)
        empty_linked_list.insert_at_beginning(node)
        assert empty_linked_list.count == 1
        assert empty_linked_list.head == node
        assert empty_linked_list.tail == node

    def test_insert_at_beginning_single_to_double(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_beginning(second_node)
        assert single_node_linked_list.head == second_node
        assert single_node_linked_list.tail == first_node

        # Create a linked list with no nodes
        #self.empty_linked_list = DoublyLinkedList()
        #assert self.empty_linked_list.head == None
        #assert self.empty_linked_list.tail == None
        #self.node = Node(1, None, None)
        #self.empty_linked_list.insert_at_beginning(self.node)
        #assert self.empty_linked_list.count == 1
        #assert self.empty_linked_list.head == self.node
        #assert self.empty_linked_list.tail == self.node

    #def test_insert_end(self):

    #def test_insert_between_two_nodes(self):

    #def test_remove_node(self):
