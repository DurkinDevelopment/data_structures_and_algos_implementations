class Node:
    __init__(self, data: None)
        self.data = data
        self.next = None

class SinglyLinkedList:
    __init__(self, head: None)
        self.head = head

    # Traverse and print the linked list
    def traverse_print(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next

    # Find the tail of the linked list
    def find_tail(self):
        curNode = self.head
        while curNode is not None:
            curNode = curNode.next
        return curNode

    # Insert node at the beginning of the list
    def insert_beginning(self, node):
        node.next = self.head
        self.head = node


    # Insert node at the end of the list
    def insert_end(self, node);
        tail = find_tail()
        tail.next = node
