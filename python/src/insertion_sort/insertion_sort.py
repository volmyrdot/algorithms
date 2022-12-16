def insertion_sort(a):
    """Sort a list or numpy array.

    Argument:
    a -- a list or numpy array
    """
    # Traverse the list or array from index 1 to n-1.
    n = len(a)
    for i in range(1, n):
        key = a[i]
        # Insert a[i] into the sorted subarray a[0:i].
        # Compare stored key with the already sorted values to its left.
        # Move each item one position to the right until we find the
        # position for the key or fall off the left end of the list or array.
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        # Insert key at the correct position in the list or array.
        a[j + 1] = key

    return a
