# sorting_algorithm.py
#
# Contains the merge sort implementation supplied as the baseline algorithm.
#
# An operation is counted each time two elements are compared during sorting.
# This definition is applied consistently across all algorithms in this experiment.
# Your implementations of bubble sort and insertion sort should count comparisons
# in the same way.
#
# Operation counts are returned as the second element of a tuple rather than
# modified in place, since Python does not support pass-by-reference for
# primitive values.
#
# To add a new algorithm, follow the same pattern as merge_sort below:
#   - Accept the array as a parameter
#   - Return a tuple of (sorted_array, operation_count)
#   - Increment operation_count each time two elements are compared


def merge_sort(array: list[int]) -> tuple[list[int], int]:
    """
    Sorts a list of integers using merge sort.
    Returns a tuple of (sorted list, operation count).
    The original list is not modified.
    """
    operation_count = 0
    result, operation_count = _merge_sort_recursive(array[:], operation_count)
    return result, operation_count


def _merge_sort_recursive(array: list[int], operation_count: int) -> tuple[list[int], int]:
    if len(array) <= 1:
        return array, operation_count

    mid = len(array) // 2
    left, operation_count = _merge_sort_recursive(array[:mid], operation_count)
    right, operation_count = _merge_sort_recursive(array[mid:], operation_count)

    merged, operation_count = _merge(left, right, operation_count)
    return merged, operation_count


def _merge(left: list[int], right: list[int], operation_count: int) -> tuple[list[int], int]:
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Each iteration performs one comparison between elements.
        operation_count += 1

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, operation_count


# --- Add your algorithms below this line ---
# Follow the same pattern as merge_sort above.
# Each algorithm should accept a list[int] and return tuple[list[int], int].
#
# Example structure (do not uncomment, implement your own):
#
# def bubble_sort(array: list[int]) -> tuple[list[int], int]:
#     arr = array[:]
#     operation_count = 0
#     # your implementation here
#     return arr, operation_count
#
# def insertion_sort(array: list[int]) -> tuple[list[int], int]:
#     arr = array[:]
#     operation_count = 0
#     # your implementation here
#     return arr, operation_count

def bubble_sort(array: list[int]) -> tuple[list[int], int]:
    arr = array[:]
    n = len(arr)
    operation_count = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            operation_count+= 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  
    return arr, operation_count

def insertion_sort(array: list[int]) -> tuple[list[int], int]:
    arr = array[:]
    n = len(arr)
    operation_count = 0

    if n <= 1:
        return arr, operation_count
    for i in range(1, n):
        key = arr[i]         
        j = i - 1
        while j >= 0 and key < arr[j]: 
            operation_count+= 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 
    return arr, operation_count