class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __repr__(self):
        string = ""

        if self.head is None:
            string += "Doubly Linked List Empty"
            return string

        string += f"Doubly Linked List:\n{self.head.data}"
        start = self.head.next
        while start is not None:
            string += f" -> {start.data}"
            start = start.next
        return string

    def append(self, data):
         if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.count += 1
        
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.count += 1

    def insert(self, data, index):
        if index > self.count or index < 0:
            raise ValueError(f"Index out of range: {index}, size: {self.count}"

    def traverse_print_from_head(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

    def traverse_print_from_tail(self):
        curNode = self.tail
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.prev

    # Insert node at the beginning of the list
    def insert_beginning(self, node):
        if node is None:
            return None
        temp = self.head
        self.head = node
        self.head.next = temp
        temp.prev = self.head
        return self.head

    # Insert node at the end of the list
    def insert_end(self, node):
        if node is None:
            return None
        temp = self.tail
        self.tail = node
        self.tail.prev = temp
        temp.next = self.tail
        return self.tail

    # Insert the new node after the middle_node
    def insert_between_two_nodes(self, middle_node, new_node):
        if middle_node is None:
            return None
        new_node.next = middle_node.next
        new_node.prev = middle_node
        middle_node.next.prev = new_node
        middle_node.next = new_node
        return new_node
    
    # Remove the node from the linked list
    def remove_node(self, node):
        # Validate that the node isn't none and the list isn't empty
        if node is None or self.head is None:
            return False

        # Validate the edge case - Head node is node to be removed
        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
            return True

        # Validate the edge case - Tail node is node to be removed
        if self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
            return True

        curNode = self.head
        prev = curNode

        # Iterate through the linked list
        while curNode is not None and curNode.next is not None:
            # Once you find the node, remove the node from the list, and return true
            if curNode is node:
                curNode.prev.next = curNode.next
                curNode.next.prev = curNode.prev
                return True

        return False

