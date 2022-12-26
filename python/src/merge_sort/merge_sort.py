def merge(a, p, q, r):
    """Merge two sorted sublists/subarrays to a larger sorted sublist/subarray.

    Arguments:
    a -- a list/array containing the sublists/subarrays to be merged
    p -- index of the beginning of the first sublist/subarray
    q -- index of the end of the first sublist/subarray;
    the second sublist/subarray starts at index q+1
    r -- ind
	"""
    # Copy the left and right sublists/subarrays.
    # If a is a list, slicing creates a copy.
    if type(a) is list:
        left = a[p: q + 1]
        right = a[q + 1: r + 1]
    # Otherwise a is a np.array, so create a copy with list().
    else:
        left = list(a[p: q + 1])
        right = list(a[q + 1: r + 1])

    i = 0  # index into left sublist/subarray
    j = 0  # index into right sublist/subarray
    k = p  # index into a[p: r+1]

    # Combine the two sorted sublists/subarrays by inserting into a
    # the lesser exposed element of the two sublists/subarrays.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    # After going through the left or right sublist/subarray, copy the
    # remainder of the other to the end of the list/array.
    if i < len(left):  # copy remainder of left
        a[k: r + 1] = left[i:]
    if j < len(right):  # copy remainder of right
        a[k: r + 1] = right[j:]


def merge_sort(a, p=0, r=None):
    """Sort the elements in the sublist/subarray a[p:r+1].

    Arguments:
    a -- a list/array containing the sublist/subarray to be merged
    p -- index of the beginning of the sublist/subarray (default = 0)
    r -- index of the end of the sublist/subarray (default = None)
    """
    # If r is not given, set to the index of the last element of the list/array.
    if r is None:
        r = len(a) - 1
    if p >= r:  # 0 or 1 element?
        return a
    q = (p + r) // 2  # midpoint of a[p: r]
    merge_sort(a, p, q)  # recursively sort a[p: q]
    merge_sort(a, q + 1, r)  # recursively sort a[q+1: r]
    merge(a, p, q, r)  # merge a[p: q] and a[q+1: r] into a[p: r]

    return a
