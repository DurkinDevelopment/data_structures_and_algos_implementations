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

# For the singly linked list, the nodes are created in descending order and then inserted at the beginning to make the linked list in ascending order
class TestDataGenerator():

    def generate_node(self, value = None, next = None, prev = None):
        new_node = Node(value, next, prev)
        return new_node

    def generate_nodes(self, count = 1):
        node_list = []
        for i in range(count):
            new_node = Node(count - i, None, None)
            node_list.append(new_node)
        return node_list

    def generate_singly_linked_list(self, length = 0):
        new_singly_linked_list = SinglyLinkedList()
        for i in range(length):
            new_node = Node(length - i, None, None)
            new_singly_linked_list.insert_at_beggining(new_node)
        return new_singly_linked_list

    def generate_singly_linked_list_from_nodes(self, node_list = []):
        new_singly_linked_list = SinglyLinkedList()
        for i in range(len(node_list)):
            node = node_list[i]
            new_singly_linked_list.insert_at_beginning(node)
        return new_singly_linked_list

class TestDataValidator():

    def validate_list_is_connected(self, linked_list):
        if linked_list.count == 0:
            assert linked_list.head == None
        elif linked_list.count == 1:
            assert linked_list.count == 1
            assert linked_list.head.data != None
            assert linked_list.head.next == None
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
        empty_list = SinglyLinkedList()
        self.validate_list_is_connected(empty_list)

    def test_traverse_print(self, capsys):
        double_node_linked_list = self.generate_singly_linked_list(2)
        self.double_node_linked_list.traverse_print()
        captured = capsys.readouterr()
        assert captured.out == "1\n2\n"

    # TODO: Create the test cases for each method (empty, single, double, triple, & quad linked list)
        # Get the test case set up for the first insert function, then copy and paste it for the rest of them
    #def test_insert_at_front_empty_list(self):

