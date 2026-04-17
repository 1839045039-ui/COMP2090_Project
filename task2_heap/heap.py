class MaxHeap:
    def __init__(self):
        self.data = []

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.data[self.parent(index)] < self.data[index]:
            p = self.parent(index)
            self.data[p], self.data[index] = self.data[index], self.data[p]
            index = p

    def extract_max(self):
        if len(self.data) == 0:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        size = len(self.data)

        while True:
            largest = index
            left = self.left(index)
            right = self.right(index)

            if left < size and self.data[left] > self.data[largest]:
                largest = left

            if right < size and self.data[right] > self.data[largest]:
                largest = right

            if largest != index:
                self.data[index], self.data[largest] = self.data[largest], self.data[index]
                index = largest
            else:
                break

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[0]

    def display(self):
        print(self.data)
