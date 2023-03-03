import random


class DLinkedList:
    def __init__(self, base_list):
        self.head = Node(base_list[0])
        self.tail = None
        self.filling(base_list)

    def filling(self, base_list):
        node = self.head
        for i in range(1, len(base_list)):
            new_node = Node(base_list[i])
            node.next = new_node
            new_node.prev = node
            node = node.next
        self.tail = node

    def print_list(self):
        node = self.head
        while node:
            if node == self.tail:
                print(node.value)
            else:
                print(node.value, ' <-> ', end='')
            node = node.next

    def length(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def find_position(self, position):
        num_len = self.length()
        if position not in range(num_len):
            return None
        if position <= num_len / 2:
            node = self.head
            now_position = 0
            counter = 1
            reverse = False
        else:
            node = self.tail
            now_position = num_len - 1
            counter = -1
            reverse = True
        while now_position != position:
            node = node.prev if reverse else node.next
            now_position += counter
        return node

    def insert(self, value, position=None):
        if position == None:
            position = self.length()
        next_node = self.find_position(position)
        prev_node = self.find_position(position - 1)
        new_node = Node(value)
        new_node.next = next_node
        new_node.prev = prev_node
        if next_node:
            next_node.prev = new_node
        else:
            self.tail = new_node
        if prev_node:
            prev_node.next = new_node
        else:
            self.head = new_node






class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

if __name__ == "__main__":
    #l = DLinkedList(random.sample(range(0, 100), 15))
    l = DLinkedList([0, 1, 2, 3, 4, 5])
    l.insert(6)
    l.print_list()
    #print(l.find_position(1))