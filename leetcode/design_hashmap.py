# https://leetcode.com/problems/design-hashmap/


# runtime 216 ms, 80%; memory 15.7 MB, 57%
class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.bucket = [None] * self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size

        if not self.bucket[index]:
            self.bucket[index] = ListNode(key , value)
        else:
            cur = self.bucket[index]

            while cur:
                if cur.key == key:
                    cur.val = value
                    return
                if not cur.next: break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.size

        cur = self.bucket[index]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.size
        prev = cur = self.bucket[index]

        if not cur: return
        if cur.key == key:
            self.bucket[index] = cur.next
            return

        cur = cur.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                break
            else:
                cur = cur.next
                prev = prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
