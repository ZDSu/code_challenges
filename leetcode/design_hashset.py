# https://leetcode.com/problems/design-hashset/


# runtime 1684 ms, 9%; memory 16.3 MB, 100%
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.set:
            self.set.append(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.set:
            self.set.remove(key)


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.set

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
