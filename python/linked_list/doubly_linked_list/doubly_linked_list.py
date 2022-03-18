class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, node = None):
        self.head = node
        self.tail = node
        self.count = 0
        if node != None:
            self.count += 1

    def __repr__(self):
        string = ""

        if self.head == None:
            string += "Doubly Linked List Empty"
            return string

        string += f"Doubly Linked List:\n{self.head.data}"
        start = self.head.next
        while start != None:
            string += f" -> {start.data}"
            start = start.next
        return string

    # Append the data as a new node at the end of the list
    def append_new_data(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            self.tail = self.head
            self.count += 1
            return node

        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node
        self.count += 1
        return node
    
    # Append a new node to the end of the list
    def append_new_node(self, node):
        if self.head == None:
            self.head = node
            self.tail = self.head
            self.count += 1
            return node

        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.count += 1
        return node

    # Insert a new node at location {index}
    def insert_new_node(self, node, index):
        # If index is out of range, raise an error
        if index > self.count or index < 0:
            raise ValueError(f"Error: Index out of range: {index}, size: {self.count}")

        if node == None:
            raise ValueError(f"Error: Node must not be null")

        if node.data == None:
            raise ValueError(f"Error: Node must have valid value")

        # Append to the end of the list
        if index == self.count:
            temp = self.tail
            temp.next = node
            node.prev = temp
            self.tail = node
            self.count += 1
            return node
       
        # Insert node at the front of the list
        if index == 0:
            self.head.prev = node
            self.head.prev = self.head
            self.head = self.head.prev
            self.count += 1
            return node

        # Starting with the head, iterate down the list {index} number of times
        start = self.head
        for _ in range(index):
            start = start.next
    
        # Once the start pointer is at the correct index, insert the node at this index
        start.prev.next = node
        start.prev.next.prev = start.prev
        start.prev.next.next = start
        self.count += 1
        return node

    # Create a new node and insert it at location {index}
    def insert_new_data(self, data, index):
        # If index is out of range, raise an error
        if index > self.count or index < 0:
            raise ValueError(f"Error: Index out of range: {index}, size: {self.count}")

        if data == None:
            raise ValueError(f"Error: Node must have valid value")

        # Append to the end of the list
        if index == self.count:
            return self.append_new_data(data)
       
        node = Node(data)

        # Insert node at the front of the list
        if index == 0:
            self.head.prev = node
            self.head.prev = self.head
            self.head = self.head.prev
            self.count += 1
            return node

        # Starting with the head, iterate down the list {index} number of times
        start = self.head
        for _ in range(index):
            start = start.next
    
        # Once the start pointer is at the correct index, insert the data as a new node at this index
        start.prev.next = node
        start.prev.next.prev = start.prev
        start.prev.next.next = start
        self.count += 1
        return node
    
    # Remove the node by index
    def remove_by_index(self, index):
        if self.count == 0:
            raise ValueError(f"Error: List is empty")

        if index >= self.count or index < 0:
            raise ValueError(f"Error: Index out of range: {index}, size: {self.count}")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
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

        start.prev.next = start.next
        start.next.prev = start.prev
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
        while curNode != None:
            print(curNode.data)
            curNode = curNode.next

    # Print the list out starting from the tail
    def traverse_print_from_tail(self):
        curNode = self.tail
        while curNode != None:
            print(curNode.data)
            curNode = curNode.prev

    # Insert the node at the beginning of the list
    def insert_at_beginning(self, node):
        if node == None:
            return None
        # Handle the edge case for adding a node to an empty list
        if self.count == 0:
            self.head = node
            self.tail = node
        # Handle the edge case for adding a node with a single node list
        elif self.count == 1:
            # Update the head pointer to point at the new node and update the head's next pointer to point at the tail node
            self.head = node
            self.head.next = self.tail
            # Update the tail pointer to point to the new head pointer
            self.tail.prev = self.head
        else: #If there are 2 or more nodes, adding to the beginning of the list functionality is the same
            temp = self.head
            self.head = node
            self.head.next = temp
            temp.prev = self.head

        self.count += 1
        return self.head

    # Insert node at the end of the list
    def insert_at_end(self, node):
        if node == None:
            return None
        # Handle the edge case for adding a node to an empty list
        if self.count == 0:
            self.head = node
            self.tail = node
        # Handle the edge case for adding a node with a single node list
        elif self.count == 1:
            # Update the tail pointer to point at the new node and update the tail's prev pointer to point at the head node
            self.tail = node
            self.tail.prev = self.head
            # Update the head pointer to point to the new tail pointer
            self.head.next = self.tail
        else: #If there are 2 or more nodes, adding to the end of the list functionality is the same
            temp = self.tail
            self.tail = node
            self.tail.prev = temp
            temp.next = self.tail

        self.count += 1
        return self.tail

    # Insert the new node after the middle_node - This is assuming the middle_node is a valid node in the doubly linked list
    def insert_between_two_nodes(self, middle_node, new_node):
        if self.count == 0:
            raise ValueError("Error: List is empty")

        if middle_node == None:
            raise ValueError("Error: Invalid middle_node")

        if new_node == None:
            raise ValueError("Error: Invalid new_node")

        if self.tail == middle_node:
            return self.insert_at_end(new_node)

        new_node.next = middle_node.next
        new_node.prev = middle_node
        middle_node.next.prev = new_node
        middle_node.next = new_node
        self.count += 1
        return new_node
    
    # Remove the node from the linked list
    def remove_by_node(self, node):
        # Validate that the list isn't empty
        if self.count == 0:
            raise ValueError("Error: List is empty")
        
        # Validate that the tail node is valid
        if self.tail == None:
            raise ValueError("Error: Tail is null")
        
        # Validate that the head node is valid
        if self.head == None:
            raise ValueError("Error: Head is null")

        # Validate that the node is not null
        if node == None: 
            raise ValueError("Error: Invalid node")

        # Validate that the node data is not null
        if node.data == None: 
            raise ValueError("Error: Invalid node data")

        if self.count == 1 and self.head == node:
            self.head = None
            self.tail = None
            self.count -= 1
            return True

        # Validate the edge case - Head node is node to be removed
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return True

        # Validate the edge case - Tail node is node to be removed
        if self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
            return True

        curNode = self.head
        prev = curNode

        # Iterate through the linked list
        while curNode != None and curNode.next != None:
            # Once you find the node, remove the node from the list, and return true
            if curNode == node:
                curNode.prev.next = curNode.next
                curNode.next.prev = curNode.prev
                self.count -= 1
                return True
            prevNode = curNode
            curNode = curNode.next

        return False

