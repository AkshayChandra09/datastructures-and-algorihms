'''
Balanced Parentheses Exercise
In this exercise you are going to apply what you learned about stacks with a real world problem. We will be using stacks
to make sure the parentheses are balanced in mathematical expressions such as:  ((32+8)∗(5/2))/(2+6).  In real life you
can see this extend to many things such as text editor plugins and interactive development environments for all sorts
of bracket completion checks.
Take a string as an input and return True if it's parentheses are balanced or False if it is not.
Try to code up a solution and pass the test cases.
'''


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


def equation_checker(equation):
    stack = Stack()
    for char in equation:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.size() != 0:
                stack.pop()
            else:
                return False
    return stack.size() == 0


# print("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
# print("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")

######################################################################################
'''Reverse Polish Notation
Reverse Polish notation, also referred to as Polish postfix notation is a way of laying out operators and operands.
When making mathematical expressions, we typically put arithmetic operators (like +, -, *, and /) between operands. For example: 5 + 7 - 3 * 8
However, in Reverse Polish Notation, the operators come after the operands. For example: 3 1 + 4 *
The above expression would be evaluated as (3 + 1) * 4 = 16
The goal of this exercise is to create a function that does the following:
Given a postfix expression as input, evaluate and return the correct final answer.
Note: In Python 3, the division operator / is used to perform float division. So for this problem, you should use int() after every division to convert the answer to an integer.
'''
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def evaluate_post_fix(input_list):
    if len(input_list) == 0:
        return 0

    stack = Stack()
    for char in input_list:
        if char.isdigit():
            stack.push(char)
        else:
            if not stack.is_empty():
                number1 = stack.pop()
            if not stack.is_empty():
                number2 = stack.pop()
            total = int(eval(number2 + char + number1))
            stack.push(str(total))

    if stack.size() > 1:
        return "Invalid Expression"

    return int(stack.pop())


# their solution
def evaluate_post_fix(input_list):
    stack = Stack()
    for element in input_list:
        if element == '*':
            second = stack.pop()
            first = stack.pop()
            output = first * second
            stack.push(output)
        elif element == '/':
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif element == '+':
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()


# d = evaluate_post_fix(["4", "13", "5", "/", "+"])
# print(d)

'''Reverse a stack. If your stack initially has 1, 2, 3, 4 (4 at the top and 1 at the bottom), 
after reversing the order must be 4, 3, 2, 1 (4 at the bottom and 1 at the top).
'''
def reverse_stack(stack):
    p = stack.head
    q = p.next
    r = q.next
    while p.next is not None:
        q.next = p
        p = q
        q = r
        r = r.next
    stack.head = p


def reverse_stack_new(stack):
    tmp_stack = Stack()
    while not stack.is_empty():
        popped = stack.pop()
        tmp_stack.push(popped)

    while not tmp_stack.is_empty():
        popped = tmp_stack.pop()
        stack.push(popped)


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# while not stack.is_empty():
#     print(stack.pop())

# reverse_stack_new(stack)
#
# while not stack.is_empty():
#     print(stack.pop())

'''Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.
For example:
For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.
If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.
'''

def minimum_bracket_traversal(input_string):
    if len(input_string) %2 == 1:
        return -1

    stack = Stack()
    for bracket in input_string:
        if stack.is_empty():
            stack.push(bracket)
        else:
            if stack.top() != bracket:
                if stack.top() == '{':
                    stack.pop()
                    continue
            stack.push(bracket)

    count = 0
    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()

        if first == '}' and second == '}':
            count += 1
        elif first == '{' and second == '{':
            count += 1
        elif first == '{' and second == '}':
            count += 2
    return count


cnt = minimum_bracket_traversal("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}")
print(cnt)