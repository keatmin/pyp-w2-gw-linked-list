from .interface import AbstractLinkedList
from .node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        if elements: #if there are elements
            for elem in elements:
                self.append(elem)

    def __str__(self):
        return "{}".format([e.elem for e in self])

    def __len__(self):
        return self.count()

    def __iter__(self):
        curr_node = self.start
        while curr_node is not None:
            yield curr_node
            curr_node = curr_node.next
        raise StopIteration
            
    def __getitem__(self, index):
        if index >= self.count():
            raise IndexError
        for i,e in enumerate(self):
            if i == index:
                return e.elem

    def __add__(self, other):
        newlist = self.__class__([el.elem for el in self])
        for el in other:
            newlist.append(el.elem)
        return newlist

    def __iadd__(self, other):
        for el in other:
            self.append(el.elem)
        return self

    def __eq__(self, other):
        a = self.start
        b = other.start
        
        while True:
            if not a and not b:
                return True
            elif not bool(a) or not bool(b):
                return False
            elif a.elem != b.elem:
                return False
            a = a.next
            b = b.next
            
    def __ne__(self, other):
        return not self.__eq__(other)
        
        
    def append(self, elem):
        add_node = Node(elem)
        if not self.start:
            self.start = add_node
            self.end = self.start
            return self.start
        
        else:
            self.end.next = add_node
            self.end = add_node
            
    def count(self):
        counter = 0
        for elem in self:
            counter += 1 
        return counter

    def pop(self, index=None):
        """ 
        1 - invalid index
        2 - index is zero
        3 - index is not zero
        """
        #1
        if len(self) == 0:
            raise IndexError
           
        if index >= len(self):
            raise IndexError
        if index is None:
            index = len(self) - 1 
        if index == 0:
            elem = self.start.elem
            self.start = self.start.next
            return elem
        
        i = 0

        prev = None
        cur = self.start

        while True:
            if i == index:
                prev.next = cur.next
                return cur.elem

            prev = cur
            cur = cur.next

            i += 1