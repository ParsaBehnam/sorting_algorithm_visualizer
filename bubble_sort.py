from swap import swap

def bubble_sort(arr):
    swapping = True
    end = len(arr)

    if len(arr) < 2:
        yield arr.copy()
        return
    
    while swapping:
        swapping = False
        for i in range(1, end):
            yield arr.copy()
            if arr[i - 1] > arr[i]:
                swap(arr, i, i - 1)
                swapping = True
                yield arr.copy()
        end -= 1

    yield arr.copy()
    