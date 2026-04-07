from swap import swap

def quick_sort(arr, low = 0, high= None):
    if high is None:
        high = len(arr) - 1

    if len(arr) <= 1:
        yield arr.copy()
        return
    
    if low < high:
        p = yield from partition(arr, low, high)
        yield from quick_sort(arr, low, p - 1)
        yield from quick_sort(arr, p + 1, high)

    yield arr.copy()


def partition(arr, low, high):
    pivot = arr[high]
    i = low -1

    for j in range(low, high):
        yield arr.copy()

        if arr[j] < pivot:
            i += 1
            swap(arr, j, i)
            yield arr.copy()
        
    swap(arr, i + 1, high)
    yield arr.copy()
    
    return i + 1
