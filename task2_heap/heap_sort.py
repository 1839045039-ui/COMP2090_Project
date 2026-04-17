from heap import MaxHeap

def heap_sort(arr):
    heap = MaxHeap()

    for value in arr:
        heap.insert(value)

    result = []
    while len(heap.data) > 0:
        result.insert(0, heap.extract_max())

    return result

if __name__ == "__main__":
    sample = [35, 12, 43, 8, 51, 27, 19]
    print("Original list:", sample)
    print("Sorted list:", heap_sort(sample))
