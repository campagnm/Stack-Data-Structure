

from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def push(self, value: object) -> None:
        """
        Add new element to top of the stack
        """
        node = SLNode(value)

        #if stack is empty create first node in the stack
        if self.is_empty() is True:
            self._head = node

        #add subsequent nodes to the top of the stack
        else:
            node.next = self._head
            self._head = node


    def pop(self) -> object:
        """
        Remove element from top of stack
        """

        #raise exception if the stack is empty
        if self.is_empty() is True:
            raise StackException()

        #get element at top of stack to return, then remove this item from the stack
        node = self._head
        self._head = self._head.next
        node.next = None

        return node.value

    def top(self) -> object:
        """
        Returns top element of stack without removing it
        """

        if self.is_empty() is True:
            raise StackException()

        #return the value of the top of the stack
        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
