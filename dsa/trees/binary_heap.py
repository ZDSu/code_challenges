"""Binary Heap Implementation (Min Heap)."""


class BinaryHeap:
    """Binary Heap class."""

    def __init__(self):
        """Constructor."""
        self.heapList = [0]
        self.size = 0

    def _percUp(self, index):
        """Percolate up."""
        while index // 2 > 0:
            if self.heapList[index] < self.heapList[index // 2]:
                # temp = self.heapList[index // 2]
                # self.heapList[i // 2] = self.heapList[index]
                # self.heapList[i] = temp
                self.heapList[index // 2], self.heapList[index] = self.heapList[index], self.heapList[index // 2]
            index = index // 2

    def insert(self, key):
        """Insert new node in heap."""
        self.heapList.append(key)
        self.size += 1
        self._percUp(self.size)

    def _percDown(self, index):
        """Percolate down."""
        while index * 2 <= self.size:
            mc_index = self._minChild(index)
            if self.heapList[index] > self.heapList[mc_index]:
                # temp = self.heapList[index]
                # self.heapList[index] = self.heapList[mc_index]
                # self.heapList[mc_index] = temp
                self.heapList[index], self.heapList[mc_index] = self.heapList[mc_index], self.heapList[index]
            index = mc_index

    def _minChild(self, index):
        """Return minimum child index."""
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heapList[index * 2] < self.heapList[index * 2 + 1]:
                return index * 2
            return index * 2 + 1

    def deleteMin(self):
        """Remove minimum child from binary heap."""
        min_value = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.size -= 1
        self._percDown(1)
        return min_value

    def buildHeap(self, arr):
        """Build a heap given a list of values."""
        self.size = len(arr)
        self.heapList = [0] + arr[:]

        index = len(arr) // 2
        while index > 0:
            self._percDown(index)
            index -= 1
