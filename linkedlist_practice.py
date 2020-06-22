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

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        next = self.head
        self.head = Node(value)
        self.head.next = next

    def search(self, value):
        current = self.head
        position = 0
        while current is not None:
            position += 1
            if current.value == value:
                return position
            current = current.next
        return None

    def remove(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            return
        prev = None
        next = current
        while current is not None:
            if current.value == value:
                prev.next = next
                break
            prev = current
            current = current.next
            next = current.next

    def pop(self):
        if self.head is None:
            return None
        item = self.head.value
        self.head = self.head.next
        return item

    def size(self):
        if self.head is None:
            return 0
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.next
        return size

    def insert(self, value, pos):
        if self.head is None:
            self.head = Node(value)
            return
        if pos == 0:
            self.prepend(value)
            return
        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return
            index += 1
            node = node.next
        else:
            self.append(value)

    # return new list
    def reverse(self):
        new_list = LinkedList()
        prev_node = None
        for value in self.to_list():
            new_node = Node(value)
            new_node.next = prev_node
            prev_node = new_node
        new_list.head = prev_node
        return new_list

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def print(self):
        current = self.head
        while current is not None:
            print("{} ".format(current.value), end="")
            current = current.next
        print()


# linkedList = LinkedList()
# # print("Appending 1,2,3,4: ")
# linkedList.append(1)
# linkedList.append(2)
# linkedList.append(3)
# linkedList.append(4)
# linkedList.append(5)
#
# linkedList.print()
#
# print("Prepending 0: ")
# linkedList.prepend(0)
# linkedList.prepend(-1)
# linkedList.print()
#
# # search
# print(linkedList.search(3))
# print(linkedList.search(7))
#
# # remove
# linkedList.remove(1)
# linkedList.remove(3)
# linkedList.print()
# # pop
# print(linkedList.pop())
# print(linkedList.pop())
# print(linkedList.pop())
# linkedList.print()
# # size
# print(linkedList.size())
# linkedList.insert(8,0)
# linkedList.print()
# # insert
# linkedList.insert(6,0)
# linkedList.print()
# reverse linked list
# reversed_list = linkedList.reverse()
# reversed_list.print()

# check if linked list is circular
# def iscircular(list_with_loop):
# #     slow = list_with_loop.head
# #     fast = list_with_loop.head
# #     while fast and fast.next:
# #         slow = slow.next
# #         fast = fast.next.next
# #         if slow == fast:
# #             return True
# #     return False
# #
# # list_with_loop = LinkedList([2, -1, 3, 0, 5])
# #
# # # Creating a loop where the last node points back to the second node
# # loop_start = list_with_loop.head.next
# #
# # node = list_with_loop.head
# # while node.next:
# #     node = node.next
# # node.next = loop_start
# #
# # # Test Cases
# #
# # # Create another circular linked list
# # small_loop = LinkedList([0])
# # small_loop.head.next = small_loop.head
# #
# # print ("Pass" if iscircular(list_with_loop) else "Fail")                  # Pass
# # print ("Pass" if iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")   # Fail
# # print ("Pass" if iscircular(LinkedList([1])) else "Fail")                 # Fail
# # print ("Pass" if iscircular(small_loop) else "Fail")                      # Pass
# # print ("Pass" if iscircular(LinkedList([])) else "Fail")                  # Fail


def print_list(head):
    current = head
    print("Linked List: ")
    while current is not None:
        print(" {} ".format(current.value), end="")
        current = current.next
    print()

'''Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers
   are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. 
    The relative order of even and odd elements must not change.
   Example:
   linked list = 1 2 3 4 5 6
   output = 1 3 5 2 4 6
 '''


def even_after_odd(head):
    if head is None:
        return None
    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None
    current = head

    while current:
        next_node = current.next
        if current.value % 2 == 0:
            if even_head is None:
                even_head = current
                even_tail = even_head
            else:
                even_tail.next = current
                even_tail = even_tail.next
        else:
            if odd_head is None:
                odd_head = current
                odd_tail = odd_head
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
        current.next = None
        current = next_node

    if odd_head is None:
        return even_head
    odd_tail.next = even_head
    return odd_head

# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(4)
# linked_list.append(6)
# linked_list.append(3)
# linked_list.append(5)
# linked_list.append(8)
# linked_list.append(7)
#
# linked_list.print()
#
# new_head = even_after_odd(linked_list.head)
#
# current = new_head
# while current is not None:
#     print("{} ".format(current.value), end="")
#     current = current.next
####################################################################################

'''
Problem Statement
You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and 
then delete the next j nodes. Continue doing so until the end of the linked list.

Example:
linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12
'''


def skip_i_delete_j(head, i, j):
    if i == 0:
        return None
    if j == 0:
        return head
    if head is None or i < 0 or j < 0:
        return head

    current = head
    previous = None

    while current:
        for x in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        for y in range(j):
            if current is None:
                break
            current = current.next

        previous.next = current

    return head


# linked_list = LinkedList([1,2,3,4,5,6,7,8,9,10,11,12])
# linked_list.print()
#
# new_head = skip_i_delete_j(linked_list.head, 2, 3)
# print_list(new_head)


def swap_nodes(head, position_one, position_two):
    if position_one == position_two:
        return head

    one_current = None
    one_previous = None

    two_current = None
    two_previous = None

    current = head
    index = 0
    new_head = None

    while current:
        if index == position_one:
            one_current = current

        if index == position_two:
            two_current = current
            break

        if one_current is None:
            one_previous = current

        two_previous = current
        index += 1
        current = current.next


    two_previous.next = one_current
    tmp = one_current.next
    one_current.next = two_current.next
    two_current.next = tmp

    if one_previous is None:
        new_head = two_current
    else:
        one_previous.next = two_current
        new_head = head

    return new_head


linked_list = LinkedList([3,4,5,2,6,1,9])
linked_list.print()

new_head = swap_nodes(linked_list.head, 3, 4)
print_list(new_head)
