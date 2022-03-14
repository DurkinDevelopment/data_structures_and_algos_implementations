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

class TestDataGenerator():
    
    def generate_node(self, value = None, next = None, prev = None):
        new_node = Node(value, next, prev)
        return new_node

    def generate_nodes(self, count = 1):
        node_list = []
        for i in range(count):
            new_node = Node(i, None, None)
            node_list.append(new_node)
        return node_list

    def generate_doubly_linked_list(self, length = 0):
        new_doubly_linked_list = DoublyLinkedList()
        for i in range(length):
            new_doubly_linked_list.append_new_data(i)
        return new_doubly_linked_list

    def generate_doubly_linked_list_from_nodes(self, node_list = []):
        new_doubly_linked_list = DoublyLinkedList()
        for i in range(len(node_list)):
            node = node_list[i]
            new_doubly_linked_list.append_new_node(node)
        return new_doubly_linked_list

class TestDoublyLinkedList(TestDataGenerator):

    def test_init_empty(self):
        empty_linked_list = self.generate_doubly_linked_list(0)
        assert empty_linked_list.head == None
        assert empty_linked_list.tail == None

    def test_init_not_empty(self):
        node_list = self.generate_nodes(1)
        single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list)
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.head.data == node_list[0].data
        assert single_node_linked_list.head.next == None
        assert single_node_linked_list.head.prev == None
        assert single_node_linked_list.tail == node_list[0]
        assert single_node_linked_list.tail.data == node_list[0].data
        assert single_node_linked_list.tail.next == None
        assert single_node_linked_list.tail.prev == None
    
    def test_traverse_print_from_head(self, capsys):
        node_list = self.generate_nodes(2)
        double_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list) 
        double_node_linked_list.traverse_print_from_head()
        captured = capsys.readouterr()
        assert captured.out == "0\n1\n"

    def test_traverse_print_from_tail(self, capsys):
        node_list = self.generate_nodes(2)
        double_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list) 
        double_node_linked_list.traverse_print_from_tail()
        captured = capsys.readouterr()
        assert captured.out == "1\n0\n"

    def test_insert_at_beginning_empty_to_single(self):
        empty_linked_list = self.generate_doubly_linked_list(0)
        assert empty_linked_list.head == None
        assert empty_linked_list.tail == None
        node = self.generate_node(1, None, None)
        empty_linked_list.insert_at_beginning(node)
        assert empty_linked_list.count == 1
        assert empty_linked_list.head == node
        assert empty_linked_list.tail == node

    def test_insert_at_beginning_single_to_double(self):
        node_list = self.generate_nodes(2)
        single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.tail == node_list[0]
        single_node_linked_list.insert_at_beginning(node_list[1])
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == node_list[1]
        assert single_node_linked_list.head.next == node_list[0]
        assert single_node_linked_list.head.prev == None
        assert single_node_linked_list.tail == node_list[0]
        assert single_node_linked_list.tail.next == None
        assert single_node_linked_list.tail.prev == node_list[1]

    def test_insert_at_beginning_double_to_triple(self):
        node_list = self.generate_nodes(3)
        doubly_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:2])
        doubly_node_linked_list.insert_at_beginning(node_list[2])
        assert doubly_node_linked_list.count == 3
        assert doubly_node_linked_list.head == node_list[2] 
        assert doubly_node_linked_list.head.prev == None
        assert doubly_node_linked_list.head.next.prev == node_list[2]
        assert doubly_node_linked_list.head.next == node_list[0] 
        assert doubly_node_linked_list.tail.prev == node_list[0]
        assert doubly_node_linked_list.tail.prev.next == node_list[1]
        assert doubly_node_linked_list.tail == node_list[1]
        assert doubly_node_linked_list.tail.next == None

    def test_insert_at_end_empty_to_single(self):
        empty_linked_list = self.generate_doubly_linked_list(0)
        assert empty_linked_list.head == None
        assert empty_linked_list.tail == None
        node = self.generate_node(1, None, None)
        empty_linked_list.insert_at_end(node)
        assert empty_linked_list.count == 1
        assert empty_linked_list.head == node
        assert empty_linked_list.tail == node

    def test_insert_at_end_single_to_double(self):
        node_list = self.generate_nodes(2)
        single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1]) 
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.tail == node_list[0]
        single_node_linked_list.insert_at_end(node_list[1])
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.head.next == node_list[1]
        assert single_node_linked_list.head.prev == None
        assert single_node_linked_list.tail == node_list[1]
        assert single_node_linked_list.tail.next == None
        assert single_node_linked_list.tail.prev == node_list[0]

    def test_insert_at_end_double_to_triple(self):
        node_list = self.generate_nodes(3)
        double_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:2]) 
        assert double_node_linked_list.count == 2
        assert double_node_linked_list.head == node_list[0]
        assert double_node_linked_list.tail == node_list[1]
        double_node_linked_list.insert_at_end(node_list[2])
        assert double_node_linked_list.count == 3
        assert double_node_linked_list.head == node_list[0]
        assert double_node_linked_list.head.next == node_list[1]
        assert double_node_linked_list.head.prev == None
        assert double_node_linked_list.head.next.next == node_list[2]
        assert double_node_linked_list.head.next.prev == node_list[0]
        assert double_node_linked_list.tail == node_list[2]
        assert double_node_linked_list.tail.prev == node_list[1]
        assert double_node_linked_list.tail.next == None

    # TODO: Cover test cases for empty, single, and double+ node lists - Also the tail pointer as the middle_node for single & double+ node list
    # DD THE ERROR HANDLING AND TEST CASES FOR IT - Each of the test coverage
    # TODO: Cover test cases for using an invalid middle_node
    # TODO: Cover test cases for using an invalid node
    def test_insert_between_two_nodes_empty_list(self):
        with pytest.raises(ValueError) as excinfo:
            empty_linked_list = self.generate_doubly_linked_list(0)
            assert empty_linked_list.head == None
            assert empty_linked_list.tail == None
            node = self.generate_node(1, None, None)
            empty_linked_list.insert_between_two_nodes(None, node)
            assert empty_linked_list.count == 0
            assert empty_linked_list.head == None
            assert empty_linked_list.tail == None
            assert str(excinfo.value) == "Error: List is empty"

    def test_insert_between_two_nodes_single_node_list_invalid_middle_node(self):
        with pytest.raises(ValueError) as excinfo:
            node_list = self.generate_nodes(2)
            single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
            assert single_node_linked_list.count == 1
            assert single_node_linked_list.head == node_list[0]
            assert single_node_linked_list.tail == node_list[0]
            single_node_linked_list.insert_between_two_nodes(None, node_list[1])
            assert single_node_linked_list.count == 1
            assert single_node_linked_list.head == node_list[0]
            assert single_node_linked_list.tail == node_list[0]
            assert str(excinfo.value) == "Error: Invalid middle_node"
            
    def test_insert_between_two_nodes_single_node_list_invalid_new_node(self):
        with pytest.raises(ValueError) as excinfo:
            node_list = self.generate_nodes(2)
            single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
            assert single_node_linked_list.count == 1
            assert single_node_linked_list.head == node_list[0]
            assert single_node_linked_list.tail == node_list[0]
            single_node_linked_list.insert_between_two_nodes(node_list[0], None)
            assert single_node_linked_list.count == 1
            assert single_node_linked_list.head == node_list[0]
            assert single_node_linked_list.tail == node_list[0]
            assert str(excinfo.value) == "Error: Invalid new_node"
            
    def test_insert_between_two_nodes_single_node_list_valid(self):
        node_list = self.generate_nodes(2)
        single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.tail == node_list[0]
        single_node_linked_list.insert_between_two_nodes(node_list[0], node_list[1])
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.tail == node_list[1]
        
    def test_insert_between_two_nodes_double_node_list_valid_nodes_after_head(self):
        node_list = self.generate_nodes(3)
        single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.tail == node_list[0]
        single_node_linked_list.insert_between_two_nodes(node_list[0], node_list[1])
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.tail == node_list[1]
        single_node_linked_list.insert_between_two_nodes(node_list[0], node_list[2])
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.head.next.prev == node_list[0]
        assert single_node_linked_list.head.next == node_list[2]
        assert single_node_linked_list.tail.prev == node_list[2]
        assert single_node_linked_list.tail.prev.next == node_list[1]
        assert single_node_linked_list.tail == node_list[1]

    def test_insert_between_two_nodes_double_node_list_valid_nodes_after_tail(self):
        node_list = self.generate_nodes(3)
        single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
        assert single_node_linked_list.count == 1
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.tail == node_list[0]
        single_node_linked_list.insert_between_two_nodes(node_list[0], node_list[1])
        assert single_node_linked_list.count == 2
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.tail == node_list[1]
        single_node_linked_list.insert_between_two_nodes(node_list[1], node_list[2])
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.head.next.prev == node_list[0]
        assert single_node_linked_list.head.next == node_list[1]
        assert single_node_linked_list.tail.prev == node_list[1]
        assert single_node_linked_list.tail.prev.next == node_list[2]
        assert single_node_linked_list.tail == node_list[2]

    def test_insert_between_two_nodes_triple_node_list_valid_nodes_after_head(self):
        node_list = self.generate_nodes(4)
        single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:3])
        single_node_linked_list.insert_between_two_nodes(node_list[0], node_list[3])
        assert single_node_linked_list.count == 4
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.head.next == node_list[3]
        assert single_node_linked_list.head.next.prev == node_list[0]
        assert single_node_linked_list.head.next.next == node_list[1]
        assert single_node_linked_list.head.next.next.prev == node_list[3]

    def test_insert_between_two_nodes_triple_node_list_valid_nodes_after_tail(self):
        node_list = self.generate_nodes(4)
        single_node_linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:3])
        single_node_linked_list.insert_between_two_nodes(node_list[0], node_list[3])
        assert single_node_linked_list.count == 4
        assert single_node_linked_list.head == node_list[0]
        assert single_node_linked_list.head.next == node_list[3]
        assert single_node_linked_list.head.next.prev == node_list[0]
        assert single_node_linked_list.head.next.next == node_list[1]
        

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
        # Insert a third node after the second node
        third_node = Node(3, None, None)
        single_node_linked_list.insert_between_two_nodes(second_node, third_node)
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev == second_node
        assert single_node_linked_list.tail.prev.next == third_node
        assert single_node_linked_list.tail == third_node
        # Insert a forth node after the middle node
        forth_node = Node(4, None, None)
        single_node_linked_list.insert_between_two_nodes(third_node, forth_node)
        assert single_node_linked_list.count == 4
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev.prev == second_node
        assert single_node_linked_list.head.next.next == third_node
        assert single_node_linked_list.tail.prev == third_node
        assert single_node_linked_list.tail.prev.next == forth_node
        assert single_node_linked_list.tail == forth_node
        
    def test_insert_between_two_nodes_triple_node_list_valid_nodes_after_middle(self):
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
        # Insert a third node after the second node
        third_node = Node(3, None, None)
        single_node_linked_list.insert_between_two_nodes(second_node, third_node)
        assert single_node_linked_list.count == 3
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev == second_node
        assert single_node_linked_list.tail.prev.next == third_node
        assert single_node_linked_list.tail == third_node
        # Insert a forth node after the middle node
        forth_node = Node(4, None, None)
        single_node_linked_list.insert_between_two_nodes(second_node, forth_node)
        assert single_node_linked_list.count == 4
        assert single_node_linked_list.head == first_node
        assert single_node_linked_list.head.next.prev == first_node
        assert single_node_linked_list.head.next == second_node
        assert single_node_linked_list.tail.prev.prev == second_node
        assert single_node_linked_list.head.next.next == forth_node
        assert single_node_linked_list.tail.prev == forth_node
        assert single_node_linked_list.tail.prev.next == third_node
        
    #def test_remove_node(self):
