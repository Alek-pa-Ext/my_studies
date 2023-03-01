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


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

if __name__ == "__main__":
    l = DLinkedList([1, 2, 3, 4, 5])
    l.print_list()