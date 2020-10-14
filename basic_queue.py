# Build queue using an array
class Queue:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()

        # enqueue new element
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1  # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0

    def front(self):
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]

        index = 0

        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        self.front_index = 0
        self.next_index = index


# q = Queue()
# q.enqueue(1)
# q.enqueue(5)
# q.enqueue(2)
# q.enqueue(7)
# q.enqueue(10)
#
# print("Size: " + str(q.size()))
# print(q.dequeue())
# print("Size: " + str(q.size()))
# print(q.dequeue())
# print("Size: " + str(q.size()))
# print(q.dequeue())


'''Build a queue using a linked list'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        if self.num_elements == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        current = self.head
        value = self.head.value
        self.head = self.head.next
        current.next = None
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def print(self):
        current = self.head
        while current:
            print(f"{current.value} ")
            current = current.next


# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
#
# queue.print()
#
# print(f"Dequeueing... {queue.dequeue()}")
# queue.print()
#
# print(f"Dequeueing... {queue.dequeue()}")
# queue.print()
#
# print(f"Dequeueing... {queue.dequeue()}")
# queue.print()



''' Build queue using Python's list'''

class Queue:
    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        value = self.list.pop()
        print(value)

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.dequeue()
# q.dequeue()


''' Reversed Queue: Write a function that takes a queue as an input and returns a reversed version of it.'''
