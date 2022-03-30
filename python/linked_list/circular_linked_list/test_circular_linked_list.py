import pytest
from circular_linked_list import Node, CircularLinkedList

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

class TestDataGenerator():

    def generate_node(self, value = None, next = None, prev = None):
        new_node = Node(value, next)
        return new_node

    def generate_nodes(self, count = 1):
        node_list = []
        for i in range(count):
            new_node = Node(i, None)
            node_list.append(new_node)
        return node_list

    def generate_linked_list(self, length = 0):
        new_linked_list = CircularLinkedList()
        for i in range(length):
            new_node = Node(i, None)
            new_linked_list.insert_at_end(new_node)
        return new_linked_list

    def generate_linked_list_from_nodes(self, node_list = []):
        new_linked_list = CircularLinkedList()
        for i in range(len(node_list)):
            node = node_list[i]
            new_linked_list.insert_at_end(node)
        return new_linked_list

class TestDataValidator():

    def validate_list_is_connected(self, linked_list):
        if linked_list.count == 0:
            assert linked_list.head == None
        elif linked_list.count == 1:
            assert linked_list.count == 1
            assert linked_list.head.data != None
            assert linked_list.head.next == None
        else:
            index = 0
            cur_node = linked_list.head
            while cur_node != None and cur_node.next != None:
                assert cur_node != None
                assert cur_node.data != None
                assert cur_node.next != None
                cur_node = cur_node.next
                index+=1

            # Validate that the count aligns with the number of nodes that were traversed
            assert index == linked_list.count - 1
            assert cur_node != None
            assert cur_node.data != None
            assert cur_node.next == None

class TestCircularLinkedList():
    
    # Insert At Front
    def insert_at_front_invalid_node_data(self):
        with pytest.raises(ValueError) as excinfo:
            data = None
            linked_list = self.generate_linked_list(1)
            linked_list.insert_at_front(data)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node data"

    def insert_at_front_empty_list(self):
        linked_list = self.generate_linked_list(0)
        data = linked_list.count
        linked_list.insert_at_front(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 1

    def insert_at_front_single_node_list(self):
        linked_list = self.generate_linked_list(1)
        data = linked_list.count
        linked_list.insert_at_front(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 2

    def insert_at_front_double_node_list(self):
        linked_list = self.generate_linked_list(2)
        data = linked_list.count
        linked_list.insert_at_front(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3

    def insert_at_front_triple_node_list(self):
        linked_list = self.generate_linked_list(3)
        data = linked_list.count
        linked_list.insert_at_front(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def insert_at_front_quad_node_list(self):
        linked_list = self.generate_linked_list(4)
        data = linked_list.count
        linked_list.insert_at_front(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    # Insert At End
    def insert_at_end_invalid_node_data(self):
        with pytest.raises(ValueError) as excinfo:
            linked_list = self.generate_linked_list(1)
            data = None
            linked_list.insert_at_end(data)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1

    def insert_at_end_empty_list(self):
        linked_list = self.generate_linked_list(0)
        data = linked_list.count
        linked_list.insert_at_end(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 1

    def insert_at_end_single_node_list(self):
        linked_list = self.generate_linked_list(1)
        data = linked_list.count
        linked_list.insert_at_end(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 2

    def insert_at_end_double_node_list(self):
        linked_list = self.generate_linked_list(2)
        data = linked_list.count
        linked_list.insert_at_end(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3

    def insert_at_end_triple_node_list(self):
        linked_list = self.generate_linked_list(3)
        data = linked_list.count
        linked_list.insert_at_end(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def insert_at_end_quad_node_list(self):
        linked_list = self.generate_linked_list(4)
        data = linked_list.count
        linked_list.insert_at_end(data)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    # Insert At Index
    def insert_at_index_invalid_node_data(self):

    def insert_at_index_invalid_index(self):

    def insert_at_index_empty_list(self):

    def insert_at_index_single_node_list(self):

    def insert_at_index_double_node_list_head(self):

    def insert_at_index_double_node_list_tail(self):

    def insert_at_index_triple_node_list_head(self):

    def insert_at_index_triple_node_list_middle(self):

    def insert_at_index_triple_node_list_tail(self):

    def insert_at_index_quad_node_list_head(self):

    def insert_at_index_quad_node_list_first_middle(self):
        
    def insert_at_index_quad_node_list_second_middle(self):

    def insert_at_index_quad_node_list_tail(self):

    # Remove By Index
    def remove_by_index_invalid_index(self):

    def remove_by_index_empty_list(self):

    def remove_by_index_single_node_list(self):

    def remove_by_index_double_node_list_head(self):

    def remove_by_index_double_node_list_tail(self):

    def remove_by_index_triple_node_list_head(self):

    def remove_by_index_triple_node_list_middle(self):

    def remove_by_index_triple_node_list_tail(self):

    def remove_by_index_quad_node_list_head(self):

    def remove_by_index_quad_node_list_first_middle(self):
        
    def remove_by_index_quad_node_list_second_middle(self):

    def remove_by_index_quad_node_list_tail(self):

    # Remove By Node
    def remove_by_node_invalid_node(self):

    def remove_by_node_invalid_node_data(self):

    def remove_by_node_invalid_index(self):

    def remove_by_node_empty_list(self):

    def remove_by_node_single_node_list(self):

    def remove_by_node_double_node_list_head(self):

    def remove_by_node_double_node_list_tail(self):

    def remove_by_node_triple_node_list_head(self):

    def remove_by_node_triple_node_list_middle(self):

    def remove_by_node_triple_node_list_tail(self):

    def remove_by_node_quad_node_list_head(self):

    def remove_by_node_quad_node_list_first_middle(self):
        
    def remove_by_node_quad_node_list_second_middle(self):

    def remove_by_node_quad_node_list_tail(self):

    # Retrieve By Index
    def retrieve_by_index_invalid_index(self):

    def retrieve_by_index_empty_list(self):

    def retrieve_by_index_single_node_list(self):

    def retrieve_by_index_double_node_list_head(self):

    def retrieve_by_index_double_node_list_tail(self):

    def retrieve_by_index_triple_node_list_head(self):

    def retrieve_by_index_triple_node_list_middle(self):

    def retrieve_by_index_triple_node_list_tail(self):

    def retrieve_by_index_quad_node_list_head(self):

    def retrieve_by_index_quad_node_list_first_middle(self):
        
    def retrieve_by_index_quad_node_list_second_middle(self):

    def retrieve_by_index_quad_node_list_tail(self):

    # Print From Head
    def print_from_head_invalid_list(self):

    def print_from_head_single_node_list(self):

    def print_from_head_double_node_list(self):

    def print_from_head_triple_node_list(self):

    def print_from_head_quad_node_list(self):

    # Print From Tail
    def print_from_tail_invalid_list(self):

    def print_from_tail_single_node_list(self):

    def print_from_tail_double_node_list(self):

    def print_from_tail_triple_node_list(self):

