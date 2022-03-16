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
    def validate_list_is_connected(self, linked_list):
        if linked_list.count == 0:
            assert linked_list.head == None
            assert linked_list.tail == None
        elif linked_list.count == 1:
            assert linked_list.count == 1
            assert linked_list.head.data != None
            assert linked_list.head.next == None
            assert linked_list.head.prev == None
            assert linked_list.head == linked_list.tail
        elif linked_list.count == 2:
            assert linked_list.count == 2
            assert linked_list.head.data != None
            assert linked_list.head.prev == None
            assert linked_list.head.next == linked_list.tail
            assert linked_list.tail.data != None
            assert linked_list.tail.next == None
            assert linked_list.tail.prev == linked_list.head
        else: 
            
            # Handle the head edge case
            assert linked_list.head.data != None
            assert linked_list.head.prev == None
            assert linked_list.head.next != None
            i = 1
            prevNode = linked_list.head
            curNode = linked_list.head.next
            
            while curNode != None and curNode.next != None:
                assert curNode.data != None
                assert curNode.prev == prevNode
                assert curNode.next != None
                prevNode = curNode
                curNode = curNode.next
                i += 1

            assert linked_list.tail.data != None
            assert linked_list.tail.prev == prevNode
            assert linked_list.tail.next == None
            i += 1
            assert linked_list.count == i

    def test_init_empty(self):
        linked_list = self.generate_doubly_linked_list(0)
        self.validate_list_is_connected(linked_list) 

    def test_init_not_empty(self):
        node_list = self.generate_nodes(1)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list)
        self.validate_list_is_connected(linked_list) 
    
    def test_traverse_print_from_head(self, capsys):
        node_list = self.generate_nodes(2)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list) 
        linked_list.traverse_print_from_head()
        captured = capsys.readouterr()
        assert captured.out == "0\n1\n"

    def test_traverse_print_from_tail(self, capsys):
        node_list = self.generate_nodes(2)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list) 
        linked_list.traverse_print_from_tail()
        captured = capsys.readouterr()
        assert captured.out == "1\n0\n"

    def test_insert_at_beginning_empty_to_single(self):
        linked_list = self.generate_doubly_linked_list(0)
        self.validate_list_is_connected(linked_list)
        node = self.generate_node(1, None, None)
        linked_list.insert_at_beginning(node)
        self.validate_list_is_connected(linked_list)

    def test_insert_at_beginning_single_to_double(self):
        node_list = self.generate_nodes(2)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
        linked_list.insert_at_beginning(node_list[1])
        self.validate_list_is_connected(linked_list)

    def test_insert_at_beginning_double_to_triple(self):
        node_list = self.generate_nodes(3)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:2])
        linked_list.insert_at_beginning(node_list[2])
        self.validate_list_is_connected(linked_list)

    def test_insert_at_end_empty_to_single(self):
        linked_list = self.generate_doubly_linked_list(0)
        node = self.generate_node(1, None, None)
        linked_list.insert_at_end(node)
        self.validate_list_is_connected(linked_list)

    def test_insert_at_end_single_to_double(self):
        node_list = self.generate_nodes(2)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1]) 
        linked_list.insert_at_end(node_list[1])
        self.validate_list_is_connected(linked_list)

    def test_insert_at_end_double_to_triple(self):
        node_list = self.generate_nodes(3)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:2]) 
        linked_list.insert_at_end(node_list[2])
        self.validate_list_is_connected(linked_list)

    def test_insert_between_two_nodes_empty_list(self):
        with pytest.raises(ValueError) as excinfo:
            node = self.generate_node(1, None, None)
            linked_list = self.generate_doubly_linked_list(0)
            linked_list.insert_between_two_nodes(None, node)
            self.validate_list_is_connected(linked_list)
            assert str(excinfo.value) == "Error: List is empty"

    def test_insert_between_two_nodes_single_node_list_invalid_middle_node(self):
        with pytest.raises(ValueError) as excinfo:
            node_list = self.generate_nodes(2)
            linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
            linked_list.insert_between_two_nodes(None, node_list[1])
            self.validate_list_is_connected(linked_list)
            assert str(excinfo.value) == "Error: Invalid middle_node"
            
    def test_insert_between_two_nodes_single_node_list_invalid_new_node(self):
        with pytest.raises(ValueError) as excinfo:
            node_list = self.generate_nodes(2)
            linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
            linked_list.insert_between_two_nodes(node_list[0], None)
            self.validate_list_is_connected(linked_list)
            assert str(excinfo.value) == "Error: Invalid new_node"
            
    def test_insert_between_two_nodes_single_node_list_valid(self):
        node_list = self.generate_nodes(2)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
        linked_list.insert_between_two_nodes(node_list[0], node_list[1])
        self.validate_list_is_connected(linked_list)
        
    def test_insert_between_two_nodes_double_node_list_valid_nodes_after_head(self):
        node_list = self.generate_nodes(3)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:2])
        linked_list.insert_between_two_nodes(node_list[0], node_list[2])
        self.validate_list_is_connected(linked_list)

    def test_insert_between_two_nodes_double_node_list_valid_nodes_after_tail(self):
        node_list = self.generate_nodes(3)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:2])
        linked_list.insert_between_two_nodes(node_list[1], node_list[2])
        self.validate_list_is_connected(linked_list)

    def test_insert_between_two_nodes_triple_node_list_valid_nodes_after_head(self):
        node_list = self.generate_nodes(4)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:3])
        linked_list.insert_between_two_nodes(node_list[0], node_list[3])
        self.validate_list_is_connected(linked_list)

    def test_insert_between_two_nodes_triple_node_list_valid_nodes_after_tail(self):
        node_list = self.generate_nodes(4)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:3])
        linked_list.insert_between_two_nodes(node_list[2], node_list[3])
        self.validate_list_is_connected(linked_list)
        
    def test_insert_between_two_nodes_triple_node_list_valid_nodes_after_middle(self):
        node_list = self.generate_nodes(4)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:3])
        linked_list.insert_between_two_nodes(node_list[1], node_list[3])
        self.validate_list_is_connected(linked_list)

    def test_remove_node_empty_list(self):
        with pytest.raises(ValueError) as excinfo:
            node_list = self.generate_nodes(1)
            linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:0])
            linked_list.remove_node(node_list[0])
            self.validate_list_is_connected(linked_list)
            assert str(excinfo.value) == "Error: List is empty"

    ## TODO: All the test cases below are a WIP, they are the template use cases that need to be updated with the specific domain logic
    def test_remove_list_invalid_node(self):
        with pytest.raises(ValueError) as excinfo:
            node_list = self.generate_nodes(2)
            linked_list = self.generate_doubly_linked_list_from_nodes(node_list[:1])
            linked_list.remove_node(node_list[1])
            self.validate_list_is_connected(linked_list)
            assert str(excinfo.value) == "Error: Invalid node"

    def test_remove_node_single_list(self):
        node_list = self.generate_nodes(1)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list)
        self.validate_list_is_connected(linked_list)
        
    def test_remove_node_double_list_from_head(self):
        node_list = self.generate_nodes(2)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list)
        self.validate_list_is_connected(linked_list)

    def test_remove_node_double_list_from_tail(self):
        node_list = self.generate_nodes(2)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list)
        self.validate_list_is_connected(linked_list)
        
    def test_remove_node_triple_list(self):
        node_list = self.generate_nodes(3)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list)
        self.validate_list_is_connected(linked_list)
        
    def test_remove_node_triple_list_from_head(self):
        node_list = self.generate_nodes(3)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list)
        self.validate_list_is_connected(linked_list)
        
    def test_remove_node_triple_list_from_middle(self):
        node_list = self.generate_nodes(3)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list)
        self.validate_list_is_connected(linked_list)
        
    def test_remove_node_triple_list_from_tail(self):
        node_list = self.generate_nodes(3)
        linked_list = self.generate_doubly_linked_list_from_nodes(node_list)
        self.validate_list_is_connected(linked_list)
