# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator=iterator
        self.next_ele=None
        self.next_ele_exist=False
        if self.iterator.hasNext():
            self.next_ele=self.iterator.next()
            self.next_ele_exist=True

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_ele

        

    def next(self):
        """
        :rtype: int
        """
        res=self.next_ele
        if self.iterator.hasNext():
            self.next_ele=self.iterator.next()
        else:
            self.next_ele_exist=False
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_ele_exist
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].