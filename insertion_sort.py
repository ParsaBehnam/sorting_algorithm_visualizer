from swap import swap

def insertion_sort(arr):
    if len(arr) <= 1:
        yield arr.copy()
        return
    for i in range(1, len(arr)):
        j = i
        yield arr.copy()
        while j > 0 and arr[j - 1] > arr[j]:
            swap(arr, j - 1, j)
            j -= 1
            yield arr.copy()
    
    yield arr.copy()


            