from swap import swap

def selection_sort(arr):
    if len(arr) <= 1:
        yield arr.copy()
        return
    for i in range(0, len(arr)):
        smallest_idx = i
        yield arr.copy()
        for j in range( i + 1, len(arr)):
            yield arr.copy()
            if arr[j] < arr[smallest_idx]:
                smallest_idx = j
        swap(arr, i, smallest_idx)
        yield arr.copy()

    yield arr.copy()