class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    # Find the tail of the linked list
    def find_tail(self):
        curNode = self.head
        while curNode.next is not None:
            curNode = curNode.next
        return curNode

    # Traverse and print the linked list
    def traverse_print_from_head(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

    # Traverse the list and create a temporary array, then increment through the temporary array backwards and print out each value
    def traverse_print_from_tail(self):
        temp_array = []
        while curNode.next is not None:
            temp_array.append(curNode)
            curNode = curNode.next
        i = len(temp_array)
        while i > 0:
            print(temp_array[i - 1].data)
            i -= 1

    # Insert node at the front of the list
    def insert_at_front(self, node):
        if node is None:
            return False
        node.next = self.head
        self.head = node
        self.count += 1
        return node

    # Insert node at the end of the list
    def insert_at_end(self, node):
        # Input Parameters - Error Handling
        if node == None:
            raise ValueError("Error: Invalid node")
        if node.data == None:
            raise ValueError("Error: Invalid node data")
        if self.count == 0: 
            self.head = node
        else:
            tail = self.find_tail()
            tail.next = node
        self.count += 1
        return node

    # Insert the new node after the middle_node
    def insert_after_node(self, existing_node, new_node):
        if middle_node is None:
            return False
        new_node.next = middle_node.next
        middle_node.next = new_node
        self.count += 1
        return node

    def insert_at_index(self, index, node):
        # Input Parameters - Error Handling
        if node == None:
            raise ValueError("Error: Invalid node")
        if node.data == None:
            raise ValueError("Error: Invalid node data")
        if index > (self.count + 1):
            raise ValueError("Error: Invalid index")

        # Input Parameters - Edge Cases
        # Insert at front of the list
        if index == 0:
            node.next = self.head
            self.head = node
        # Insert after the head node
        elif index == 1:
            node.next = self.head.next
            self.head.next = node
        else: # Else iterate through the list until you've reached the index and then insert the new node
            cur_node = self.head.next
            prev_node = self.head
            count = 0
            while cur_node != None:
                if count == index:
                    break
                prev_node = cur_node
                cur_node = cur_node.next
                count += 1
            prev_node.next = node
            node.next = cur_node
        # Increment the total count by 1
        self.count += 1
        return node

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

#TODO:    def remove_node_by_index(self, index):

#TODO:    def retrieve_node_by_index(self, index):
