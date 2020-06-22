class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        if self.tail is None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)
            self.tail = current.next
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def print(self):
        current = self.head
        while current is not None:
            print("{} ".format(current.value), end="")
            current = current.next
        print()


# pascal triangle
def nth_row_pascal(n):
    if n == 0:
        return [1]

    current_row = [1]
    for i in range(1, n+1):
        prev_row = current_row
        current_row = [1]
        for j in range(1, i):
            next_number = prev_row[j] + prev_row[j-1]
            current_row.append(next_number)
        current_row.append(1)
    return current_row

print(nth_row_pascal(4))




