

from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        """
        return not self._head.next

    def insert_front(self, value: object) -> None:
        """
        Adds new node at beginning of list (right after sentinel)
        """
        #if list is empty create head node after sentinel
        if self.is_empty() is True:
            self._head.next = SLNode(value)

        #create a new node and add it to the front after sentinel node
        else:
            new_node = SLNode(value)
            new_node.next = self._head.next
            self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        Adds new node to end of linked list
        """

        node = self._head.next

        if self.is_empty() is True:
            self._head.next = SLNode(value)

        #traverse to end of the linked list to insert new node at end
        else:
            for count in range(self.length()):
                if node.next is None:
                    node.next = SLNode(value)

                node = node.next


    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new value at a specified index
        """

        #if index is invalid raise exception
        if index < 0 or index > self.length():
            raise SLLException()

        node = SLNode(value)

        if self.is_empty() is True:
            self._head.next = SLNode(value)

        #if index is at beginning of list make new node the head node after sentinel
        elif index == 0:
            node.next = self._head.next
            self._head.next = node

        #traverse list to index that new node is to be inserted
        else:
            insert_node = self._head.next

            for count in range(index - 1):
                if count is not None:
                    insert_node = insert_node.next

            if insert_node is not None:

                node.next = insert_node.next
                insert_node.next = node


    def remove_at_index(self, index: int) -> None:
        """
        Removes node at specified index position from linked list
        """

        #raise exception if index is invalid
        if index < 0 or index >= self.length() or self.is_empty() is True or isinstance(index, LinkedList):
            raise SLLException()

        #if index is at the beginning of the list
        if self._head.next is not None and index == 0:
            node_delete = self._head.next
            self._head.next = self._head.next.next
            node_delete is None

        #traverse list to required index and remove that node
        else:
            node = self._head.next

            for count in range(index - 1):
                if count is not None:
                    node = node.next

            if node is not None and node.next is not None:
                node_delete = node.next
                node.next = node.next.next
                node_delete is None

    def remove(self, value: object) -> bool:
        """
        Traverse list and remove first node that matches the provided value of object.  If removed, return True
        """

        index = 0
        node = self._head.next

        #traverse list and call remove_at_index to remove node at the value requested
        for count in range(self.length()):
            if value == node.value:
                self.remove_at_index(index)
                return True

            #return false if value is not found
            elif node.value is None:
                return False

            node = node.next
            index += 1

        return False


    def count(self, value: object) -> int:
        """
        Counts number of elements in the list that match a provided value and returns this number
        """

        node = self._head.next

        #if empty list return 0 count
        if self.is_empty() is True:
            return 0

        count_element = 0

        #traverse the list and increment the counter each time the value is encountered
        for count in range(self.length()):
            if node.value == value:
                count_element += 1

            node = node.next

        return count_element

    def find(self, value: object) -> bool:
        """
        Returns boolean value based on whether or not the provided value exists in the list
        """

        node = self._head.next

        #if list is empty return false
        if self.is_empty() is True:
            return False

        #traverse list and return true if value is in list
        else:
            for count in range(self.length()):
                if node.value == value:
                    return True

                node = node.next

            return False


    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Return new LinkedList containing requested number of nodes from original list starting with node at requested
        start index
        """

        #check for validity of input parameters
        if start_index < 0 or size > self.length() or size > self.length() - start_index or size < 0 or start_index > self.length() - 1:
            raise SLLException()

        #create new linked list with sliced list
        node = self._head.next
        slice_list = LinkedList()
        end_index = start_index + size

        #get to the part of the linked list where the slice is to start
        for count in range(start_index):
            node = node.next

        #copy the sliced part to the new list to return
        for count in range(start_index, end_index, 1):
            node_value = node.value
            slice_list.insert_back(node_value)
            node = node.next

        return slice_list

if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
