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
        while curNode.next != None:
            curNode = curNode.next
        return curNode

    # Traverse and print the linked list
    def traverse_print_from_head(self):
        curNode = self.head
        while curNode != None:
            print(curNode.data)
            curNode = curNode.next

    # Traverse the list and create a temporary array, then increment through the temporary array backwards and print out each value
    def traverse_print_from_tail(self):
        if self.count == 0:
            return

        temp_array = []
        curNode = self.head

        while curNode != None:
            temp_array.append(curNode)
            curNode = curNode.next

        length = len(temp_array)
        index = 1

        while index <= length:
            print(temp_array[length - index].data)
            index += 1

    # Insert node at the front of the list
    def insert_at_front(self, node):
        # Input Parameters - Error Handling
        if node == None:
            raise ValueError("Error: Invalid node")
        if node.data == None:
            raise ValueError("Error: Invalid node data")

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

    # Insert the new node after the existing node
    def insert_after_node(self, existing_node, new_node):
        if self.count == 0:
            raise ValueError("Error: Invalid list length")
        # Input Parameters - Error Handling
        if existing_node == None or new_node == None:
            raise ValueError("Error: Invalid node")
        if existing_node.data == None or new_node.data == None:
            raise ValueError("Error: Invalid node data")
        new_node.next = existing_node.next
        existing_node.next = new_node
        self.count += 1
        return new_node

    def insert_at_index(self, index, node):
        # Input Parameters - Error Handling
        if node == None:
            raise ValueError("Error: Invalid node")
        if node.data == None:
            raise ValueError("Error: Invalid node data")
        if index == None or index > (self.count + 1):
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
    def remove_by_node(self, node):
        if self.count == 0:
            raise ValueError("Error: Invalid list size")
        if node == None:
            raise ValueError("Error: Invalid node")
        if node.data == None:
            raise ValueError("Error: Invalid node data")

        # Edge Case - Handle the head node
        if self.head == node:
            self.head = self.head.next
            self.count -= 1
            return

        prev_node = self.head
        cur_node = self.head.next

        # Validate the edge case - Head node is node to be removed
        while cur_node != None:
            if cur_node == node:
                prev_node.next = cur_node.next
                self.count -= 1
                return
            else:
                prev_node = cur_node
                cur_node = cur_node.next
        
        # Edge Case - Handle the node isn't in the list case
        raise ValueError("Error: Node not found")


    def remove_by_index(self, index):
        if self.count == 0:
            raise ValueError("Error: Invalid list size")
        if index >= self.count or index < 0:
            raise ValueError("Error: Invalid index")

        if index == 0:
            # Get the node, update the list, update the node, & return the node
            node = self.head
            self.head = self.head.next
            node.next = None
            self.count -= 1
            return node

        cur_node = self.head.next
        prev_node = self.head
        cur_index = 1
        while cur_index != index:
            prev_node = cur_node
            cur_node = cur_node.next
            cur_index += 1
        
        # Update the list, update the node, & then return the node
        prev_node.next = cur_node.next
        cur_node.next = None
        self.count -= 1
        return cur_node
            
    def retrieve_by_index(self, index):
        if self.count == 0:
            raise ValueError("Error: Invalid list size")
        if index >= self.count or index < 0:
            raise ValueError("Error: Invalid index")

        cur_node = self.head
        cur_index = 0

        while cur_index != index: 
            cur_node = cur_node.next
            cur_index += 1

        return cur_node
