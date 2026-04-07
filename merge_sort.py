def merge_sort(arr):
    if len(arr) <= 1:
        yield arr.copy()
        return arr

    mid = len(arr) // 2

    
    left_gen = merge_sort(arr[:mid])
    left = None
    for state in left_gen:
        left = state
        yield state

    right_gen = merge_sort(arr[mid:])
    right = None
    for state in right_gen:
        right = state
        yield state

    # merge step
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1
        yield arr.copy()

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        yield arr.copy()

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        yield arr.copy()

    return arr