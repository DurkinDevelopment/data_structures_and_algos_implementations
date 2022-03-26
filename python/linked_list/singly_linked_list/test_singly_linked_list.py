import pytest
from singly_linked_list import Node, SinglyLinkedList

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

# For the singly linked list, the nodes are created in descending order and then inserted at the front to make the linked list in ascending order
class TestDataGenerator():

    def generate_node(self, value = None, next = None, prev = None):
        new_node = Node(value, next)
        return new_node

    def generate_nodes(self, count = 1):
        node_list = []
        for i in range(count):
            new_node = Node(count - i, None)
            node_list.append(new_node)
        return node_list

    def generate_singly_linked_list(self, length = 0):
        new_singly_linked_list = SinglyLinkedList()
        for i in range(length):
            new_node = Node(length - i, None)
            new_singly_linked_list.insert_at_front(new_node)
        return new_singly_linked_list

    def generate_singly_linked_list_from_nodes(self, node_list = []):
        new_singly_linked_list = SinglyLinkedList()
        for i in range(len(node_list)):
            node = node_list[i]
            new_singly_linked_list.insert_at_front(node)
        return new_singly_linked_list

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

class TestSinglyLinkedList(TestDataGenerator, TestDataValidator):
    def test_init_empty(self):
        empty_list = self.generate_singly_linked_list(0)
        self.validate_list_is_connected(empty_list)

    def test_traverse_print(self, capsys):
        double_node_linked_list = self.generate_singly_linked_list(2)
        double_node_linked_list.traverse_print_from_head()
        captured = capsys.readouterr()
        assert captured.out == "1\n2\n"

    #insert at front
    def test_insert_at_front_invalid_param_list_null_node(self):
        with pytest.raises(ValueError) as excinfo:
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_at_front(None)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node"

    def test_insert_at_front_invalid_param_list_null_node_data(self):
        with pytest.raises(ValueError) as excinfo:
            node = self.generate_node(None, None, None)
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_at_front(node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node data"

    def test_insert_at_front_empty_list(self):
        node = self.generate_node(1, None, None)
        linked_list = self.generate_singly_linked_list(0)
        linked_list.insert_at_front(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 1

    def test_insert_at_front_single_node_list(self):
        node = self.generate_node(2, None, None)
        linked_list = self.generate_singly_linked_list(1)
        linked_list.insert_at_front(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 2

    def test_insert_at_front_double_node_list(self):
        node = self.generate_node(3, None, None)
        linked_list = self.generate_singly_linked_list(2)
        linked_list.insert_at_front(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3
        
    def test_insert_at_front_triple_node_list(self):
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_front(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_at_front_quad_node_list(self):
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_front(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    #insert at end
    def test_insert_at_end_invalid_param_list_null_node(self):
        with pytest.raises(ValueError) as excinfo:
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_at_end(None)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node"

    def test_insert_at_end_invalid_param_list_null_node_data(self):
        with pytest.raises(ValueError) as excinfo:
            node = self.generate_node(None, None, None)
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_at_end(node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node data"

    def test_insert_at_end_empty_list(self):
        node = self.generate_node(1, None, None)
        linked_list = self.generate_singly_linked_list(0)
        linked_list.insert_at_end(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 1

    def test_insert_at_end_single_node_list(self):
        node = self.generate_node(2, None, None)
        linked_list = self.generate_singly_linked_list(1)
        linked_list.insert_at_end(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 2

    def test_insert_at_end_double_node_list(self):
        node = self.generate_node(3, None, None)
        linked_list = self.generate_singly_linked_list(2)
        linked_list.insert_at_end(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3
        
    def test_insert_at_end_triple_node_list(self):
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_end(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_at_end_quad_node_list(self):
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_end(node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    # insert at index
    def test_insert_at_index_invalid_param_null_node(self):
        with pytest.raises(ValueError) as excinfo:
            index = 0
            node = None
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_at_index(index, node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node"

    def test_insert_at_index_invalid_param_null_node_data(self):
        with pytest.raises(ValueError) as excinfo:
            index = 0
            node = self.generate_node(None, None, None)
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_at_index(index, node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node data"

    def test_insert_at_index_invalid_param_null_index(self):
        with pytest.raises(ValueError) as excinfo:
            index = None
            node = self.generate_node(2, None, None)
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_at_index(index, node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 2
        assert str(excinfo.value) == "Error: Invalid index"

    def test_insert_at_index_invalid_param_index_out_of_bounds(self):
        with pytest.raises(ValueError) as excinfo:
            index = 3
            node = self.generate_node(2, None, None)
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_at_index(index, node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid index"

    def test_insert_at_index_empty_list(self):
        index = 0
        node = self.generate_node(1, None, None)
        linked_list = self.generate_singly_linked_list(0)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 1

    def test_insert_at_index_single_node_list_front(self):
        index = 0
        node = self.generate_node(2, None, None)
        linked_list = self.generate_singly_linked_list(1)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 2

    def test_insert_at_index_single_node_list_next_last(self):
        index = 1
        node = self.generate_node(2, None, None)
        linked_list = self.generate_singly_linked_list(1)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 2

    def test_insert_at_index_double_node_list_front(self):
        index = 0
        node = self.generate_node(3, None, None)
        linked_list = self.generate_singly_linked_list(2)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3

    def test_insert_at_index_double_node_list_first_middle(self):
        index = 1 
        node = self.generate_node(3, None, None)
        linked_list = self.generate_singly_linked_list(2)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3

    def test_insert_at_index_double_node_list_second_middle(self):
        index = 2 
        node = self.generate_node(3, None, None)
        linked_list = self.generate_singly_linked_list(2)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3
        
    def test_insert_at_index_double_node_list_last(self):
        index = 3 
        node = self.generate_node(3, None, None)
        linked_list = self.generate_singly_linked_list(2)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3

    def test_insert_at_index_triple_node_list_front(self):
        index = 0
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_at_index_triple_node_list_first_middle(self):
        index = 1
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_at_index_triple_node_list_second_middle(self):
        index = 2
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4
        
    def test_insert_at_index_triple_node_list_third_middle(self):
        index = 3
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_at_index_triple_node_list_last(self):
        index = 4
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_at_index_triple_node_list_front(self):
        index = 0
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    def test_insert_at_index_triple_node_list_first_middle(self):
        index = 1
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    def test_insert_at_index_triple_node_list_second_middle(self):
        index = 2
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5
        
    def test_insert_at_index_triple_node_list_third_middle(self):
        index = 3
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    def test_insert_at_index_triple_node_list_forth_middle(self):
        index = 4
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    def test_insert_at_index_triple_node_list_last(self):
        index = 5
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    #insert after node
    def test_insert_after_node_invalid_param_null_existing_node(self):
        with pytest.raises(ValueError) as excinfo:
            existing_node = None
            new_node = self.generate_node(3, None, None)
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_after_node(existing_node, new_node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node"

    def test_insert_after_node_invalid_param_null_existing_node_data(self):
        with pytest.raises(ValueError) as excinfo:
            existing_node = self.generate_node(None, None, None)
            new_node = self.generate_node(3, None, None)
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_after_node(existing_node, new_node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node data"

    def test_insert_after_node_invalid_param_null_new_node(self):
        with pytest.raises(ValueError) as excinfo:
            existing_node = self.generate_node(3, None, None)
            new_node = None 
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_after_node(existing_node, new_node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node"

    def test_insert_after_node_invalid_param_null_new_node_data(self):
        with pytest.raises(ValueError) as excinfo:
            existing_node = self.generate_node(3, None, None)
            new_node = self.generate_node(None, None, None)
            linked_list = self.generate_singly_linked_list(1)
            linked_list.insert_after_node(existing_node, new_node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 1
        assert str(excinfo.value) == "Error: Invalid node data"

    def test_insert_after_node_invalid_list_length(self):
        with pytest.raises(ValueError) as excinfo:
            existing_node = self.generate_node(3, None, None)
            new_node = self.generate_node(None, None, None)
            linked_list = self.generate_singly_linked_list(0)
            linked_list.insert_after_node(existing_node, new_node)
            self.validate_list_is_connected(linked_list)
            assert linked_list.count == 0
        assert str(excinfo.value) == "Error: Invalid list length"

    def test_insert_after_node_single_node_list_after_head(self):
        node_list = self.generate_nodes(1)
        linked_list = self.generate_singly_linked_list_from_nodes(node_list)
        existing_node = node_list[0]
        new_node = self.generate_node(3, None, None)
        linked_list.insert_after_node(existing_node, new_node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 2

    def test_insert_after_node_double_node_list_after_head(self):
        node_list = self.generate_nodes(2)
        linked_list = self.generate_singly_linked_list_from_nodes(node_list)
        existing_node = node_list[0]
        new_node = self.generate_node(3, None, None)
        linked_list.insert_after_node(existing_node, new_node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3

    def test_insert_after_node_double_node_list_after_tail(self):
        node_list = self.generate_nodes(2)
        linked_list = self.generate_singly_linked_list_from_nodes(node_list)
        existing_node = node_list[1]
        new_node = self.generate_node(3, None, None)
        linked_list.insert_after_node(existing_node, new_node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3

    def test_insert_after_node_double_node_list_second_middle(self):
        index = 2 
        node = self.generate_node(3, None, None)
        linked_list = self.generate_singly_linked_list(2)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3
        
    def test_insert_after_node_double_node_list_last(self):
        index = 3 
        node = self.generate_node(3, None, None)
        linked_list = self.generate_singly_linked_list(2)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 3

    def test_insert_after_node_triple_node_list_front(self):
        index = 0
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_after_node_triple_node_list_first_middle(self):
        index = 1
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_after_node_triple_node_list_second_middle(self):
        index = 2
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4
        
    def test_insert_after_node_triple_node_list_third_middle(self):
        index = 3
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_after_node_triple_node_list_last(self):
        index = 4
        node = self.generate_node(4, None, None)
        linked_list = self.generate_singly_linked_list(3)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 4

    def test_insert_after_node_triple_node_list_front(self):
        index = 0
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    def test_insert_after_node_triple_node_list_first_middle(self):
        index = 1
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    def test_insert_after_node_triple_node_list_second_middle(self):
        index = 2
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5
        
    def test_insert_after_node_triple_node_list_third_middle(self):
        index = 3
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    def test_insert_after_node_triple_node_list_forth_middle(self):
        index = 4
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    def test_insert_after_node_triple_node_list_last(self):
        index = 5
        node = self.generate_node(5, None, None)
        linked_list = self.generate_singly_linked_list(4)
        linked_list.insert_at_index(index, node)
        self.validate_list_is_connected(linked_list)
        assert linked_list.count == 5

    # remove by index
    # remove by node
    # retrieve by index
    # traverse from end
