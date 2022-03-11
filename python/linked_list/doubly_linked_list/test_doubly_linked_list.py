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
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node at the beginning of the list
        second_node = Node(2, None, None)
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_beginning(second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == second_node
        assert single_node_linked_list.tail == first_node

    def test_insert_at_beginning_double_to_triple(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node at the beginning of the list
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_beginning(second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == second_node
        assert single_node_linked_list.tail == first_node
        # Insert another new node at the beginning of the list
        third_node = Node(3, None, None)
        single_node_linked_list.insert_at_beginning(third_node)
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == third_node
        assert single_node_linked_list.head.next.prev == third_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev == second_node
        assert single_node_linked_list.tail.prev.next == first_node
        assert single_node_linked_list.tail == first_node

    def test_insert_at_end_empty_to_single(self):
        # Create a linked list with no nodes
        empty_linked_list = DoublyLinkedList()
        assert empty_linked_list.head == None
        assert empty_linked_list.tail == None
        # Create a new node and insert it at the end of the empty list
        node = Node(1, None, None)
        empty_linked_list.insert_at_end(node)
        assert empty_linked_list.count == 1
        assert empty_linked_list.head == node
        assert empty_linked_list.tail == node

    def test_insert_at_end_single_to_double(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node at the end of the list
        second_node = Node(2, None, None)
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_end(second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == second_node

    def test_insert_at_end_double_to_triple(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node at the end of the list
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_end(second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == first_node 
        assert single_node_linked_list.tail == second_node
        # Insert another new node at the end of the list
        third_node = Node(3, None, None)
        single_node_linked_list.insert_at_end(third_node)
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev == second_node
        assert single_node_linked_list.tail.prev.next == third_node
        assert single_node_linked_list.tail == third_node

    # TODO: Cover test cases for empty, single, and double+ node lists - Also the tail pointer as the middle_node for single & double+ node list
    # DD THE ERROR HANDLING AND TEST CASES FOR IT - Each of the test coverage
    # TODO: Cover test cases for using an invalid middle_node
    # TODO: Cover test cases for using an invalid node
    def test_insert_between_two_nodes_empty_list(self):
        with pytest.raises(ValueError) as excinfo:
            # Create a linked list with no nodes
            empty_linked_list = DoublyLinkedList()
            assert empty_linked_list.head == None
            assert empty_linked_list.tail == None
            # Create a new node and insert it at the end of the empty list
            node = Node(1, None, None)
            empty_linked_list.insert_between_two_nodes(None, node)
            assert empty_linked_list.count == 0
            assert empty_linked_list.head == None
            assert empty_linked_list.tail == None
            assert str(excinfo.value) == "Error: List is empty"

    def test_insert_between_two_nodes_single_node_list_invalid_middle_node(self):
        with pytest.raises(ValueError) as excinfo:
            # Create a linked list with a single node
            first_node = Node(1, None, None)
            single_node_linked_list = DoublyLinkedList(first_node)
            assert single_node_linked_list.count == 1
            assert single_node_linked_list.head == first_node
            assert single_node_linked_list.tail == first_node
            # Try and insert a new node after an invalid middle_node 
            second_node = Node(2, None, None)
            single_node_linked_list.insert_between_two_nodes(None, second_node)
            assert single_node_linked_list.count == 1
            assert single_node_linked_list.head == first_node
            assert single_node_linked_list.tail == first_node
            assert str(excinfo.value) == "Error: Invalid middle_node"
            
    def test_insert_between_two_nodes_single_node_list_invalid_new_node(self):
        with pytest.raises(ValueError) as excinfo:
            # Create a linked list with a single node
            first_node = Node(1, None, None)
            single_node_linked_list = DoublyLinkedList(first_node)
            assert single_node_linked_list.count == 1
            assert single_node_linked_list.head == first_node
            assert single_node_linked_list.tail == first_node
            # Try and insert a invalid node after the first node
            second_node = Node(2, None, None)
            single_node_linked_list.insert_between_two_nodes(first_node, None)
            assert single_node_linked_list.count == 1
            assert single_node_linked_list.head == first_node
            assert single_node_linked_list.tail == first_node
            assert str(excinfo.value) == "Error: Invalid new_node"
            
    def test_insert_between_two_nodes_single_node_list_valid(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node after the first node
        second_node = Node(2, None, None)
        single_node_linked_list.insert_between_two_nodes(first_node, second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == second_node
        
    def test_insert_between_two_nodes_double_node_list_valid_nodes_after_head(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.count == 0
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node at the end of the list
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_end(second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == first_node 
        assert single_node_linked_list.tail == second_node
        # Insert another new node at the end of the list
        third_node = Node(3, None, None)
        single_node_linked_list.insert_at_end(third_node)
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev == second_node
        assert single_node_linked_list.tail.prev.next == third_node
        assert single_node_linked_list.tail == third_node

    def test_insert_between_two_nodes_double_node_list_valid_nodes_after_tail(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.count == 0
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node at the end of the list
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_end(second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == first_node 
        assert single_node_linked_list.tail == second_node
        # Insert another new node at the end of the list
        third_node = Node(3, None, None)
        single_node_linked_list.insert_at_end(third_node)
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev == second_node
        assert single_node_linked_list.tail.prev.next == third_node

    def test_insert_between_two_nodes_triple_node_list_valid_nodes_after_head(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.count == 0
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node at the end of the list
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_end(second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == first_node 
        assert single_node_linked_list.tail == second_node
        # Insert another new node at the end of the list
        third_node = Node(3, None, None)
        single_node_linked_list.insert_at_end(third_node)
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev == second_node
        assert single_node_linked_list.tail.prev.next == third_node

    def test_insert_between_two_nodes_triple_node_list_valid_nodes_after_tail(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.count == 0
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node at the end of the list
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_end(second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == first_node 
        assert single_node_linked_list.tail == second_node
        # Insert another new node at the end of the list
        third_node = Node(3, None, None)
        single_node_linked_list.insert_at_end(third_node)
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev == second_node
        assert single_node_linked_list.tail.prev.next == third_node
        
    def test_insert_between_two_nodes_triple_node_list_valid_nodes_after_middle(self):
        # Create a linked list with a single node
        first_node = Node(1, None, None)
        single_node_linked_list = DoublyLinkedList(first_node)
        assert single_node_linked_list.count == 0
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.tail == first_node
        # Insert a new node at the end of the list
        second_node = Node(2, None, None)
        single_node_linked_list.insert_at_end(second_node)
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == first_node 
        assert single_node_linked_list.tail == second_node
        # Insert another new node at the end of the list
        third_node = Node(3, None, None)
        single_node_linked_list.insert_at_end(third_node)
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev == second_node
        assert single_node_linked_list.tail.prev.next == third_node

    #def test_remove_node(self):
