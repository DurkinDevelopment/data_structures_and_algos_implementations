class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, head = Node()):
        self.head = head

    # Traverse and print the linked list
    def traverse_print_from_head(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

    # Find the tail of the linked list
    def find_tail(self):
        curNode = self.head
        while curNode.next is not None:
            curNode = curNode.next
        return curNode

    def traverse_print_from_tail(self):

    # Insert node at the beginning of the list
    def insert_at_beginning(self, node):
        if node is None:
            return False
        node.next = self.head
        self.head = node
        return True


    # Insert node at the end of the list
    def insert_at_end(self, node):
        if node is None:
            return False
        tail = find_tail()
        tail.next = node
        return True

    # Insert the new node after the middle_node
    def insert_after_node(self, existing_node, new_node):
        if middle_node is None:
            return False
        new_node.next = middle_node.next
        middle_node.next = new_node
        return True

    def insert_at_index(self, index):
    
    # Remove the node from the linked list
    def remove_node_by_node(self, node):
        curNode = self.head

        # Validate the edge case - Head node is node to be removed
        if curNode is not None:
            if curNode is node:
                self.head = curNode.next
                curNode = None
                return True

        # Iterate through the linked list
        while curNode is not None:
            # Once you find the node, break from the loop
            if curNode is node:
                break
            prev = curNode
            curNode = curNode.next

        if curNode is None:
            return False

        prev.next = curNode.next
        curNode = None

    def remove_node_by_index(self, index):

    def retrieve_node_by_index(self, index):
