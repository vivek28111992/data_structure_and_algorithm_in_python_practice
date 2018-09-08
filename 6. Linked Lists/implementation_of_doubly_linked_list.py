# Implementation of Doubly Linked List
# A base class for managing a doubly linked list.

class _DoublyLinkedBase:
    """A base class providing a doubly linked list representattion."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'                 # streamlined memory usage

        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer              # trailer is after header
        self._trailer._prev = self._header              # header is before trailer
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                             # record deleted element
        node._prev = node._next = node._element = None      # deprecated node
        return element                                      # return deleted element
  