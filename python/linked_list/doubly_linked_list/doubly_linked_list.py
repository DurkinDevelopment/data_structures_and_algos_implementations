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
        while start != None:
            string += f" -> {start.data}"
            start = start.next
        return string

    # Append the data as a new node at the end of the list
    def append(self, data):
         if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.count += 1
        
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.count += 1

    # Insert a new node with the data at location {index}
    def insert(self, data, index):
        # If index is out of range, raise an error
        if index > self.count or index < 0:
            raise ValueError(f"Index out of range: {index}, size: {self.count}"

        # Append to the end of the list
        if index == self.count:
            self.append(data)
            return 
       
        # Insert node at the front of the list
        if index == 0:
            self.head.previous = Node(data)
            self.head.previous = self.head
            self.head = self.head.previous
            self.count += 1
            return

        # Starting with the head, iterate down the list {index} number of times
        start = self.head
        for _ in range(index):
            start = start.next
    
        # Once the start pointer is at the correct index, insert the data as a new node at this index
        start.previous.next = Node(data)
        start.previous.next.previous = start.previous
        start.previous.next.next = start
        self.count += 1
        return
    
    # Remove the node by index
    def remove(self, index):
        if index >= self.count or index < 0
            raise ValueError(f"Index out of range: {index}, size: {self.count}")

        if index == 0:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
            return

        if index == (self.count - 1):
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
            return

        start = self.head
        for _ in range(index):
            start = start.next

        start.previous.next = start.next
        start.next.previous = start.previous
        self.count -= 1
        return

    # Get the index of the first node with the data
    def index_by_data(self, data):
        start = self.head
        for i in range(self.count):
            if start.data == data:
                return i
            start = start.next
        return None

    # Get the index of the node
    def index_by_node(self, node):
        start = self.head
        for i in range(self.count):
            if start == node:
                return i
            start = start.next
        return None

    # Print the size of the list
    def size(self):
        return self.count

    # Print the class
    def display(self):
        print(self)

    # Print the list out starting from the head
    def traverse_print_from_head(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

    # Print the list out starting from the tail
    def traverse_print_from_tail(self):
        curNode = self.tail
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.prev

    # Insert the node at the beginning of the list
    def insert_at_beginning(self, node):
        if node is None:
            return None
        temp = self.head
        self.head = node
        self.head.next = temp
        temp.prev = self.head
        return self.head

    # Insert node at the end of the list
    def insert_at_end(self, node):
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

