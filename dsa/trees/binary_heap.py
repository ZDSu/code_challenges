"""Binary Heap Implementation."""


class BinaryHeap:
    """Binary Heap class."""

    def __init__(self):
        """Constructor."""
        self.heapList = [0]
        self.size = 0

    def percUp(self, index):
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
        self.percUp(self.size)

    def percDown(self, index):
        """Percolate down."""
        while index * 2 <= self.size:
            mc_index = self.minChild(index)
            if self.heapList[index] > self.heapList[mc_index]:
                # temp = self.heapList[index]
                # self.heapList[index] = self.heapList[mc_index]
                # self.heapList[mc_index] = temp
                self.heapList[index], self.heapList[mc_index] = self.heapList[mc_index], self.heapList[index]
            index = mc_index

    def minChild(self, index):
        """Return minimum child index."""
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heapList[index * 2] < self.heapList[index * 2 + 1]:
                return index * 2
            return index * 2 + 1
