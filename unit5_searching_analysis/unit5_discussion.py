"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    Searches through the list from beginning to end.
    Returns the index of the target if found, or -1 if not found.
    """

    # Linear search checks each item one at a time.
    # In the worst case, every element must be checked.
    # Therefore, linear search has O(n) time complexity.
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


def binary_search(lst, target):
    """
    Searches a sorted list using binary search.
    Returns the index of the target if found, or -1 if not found.
    """

    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = (low + high) // 2

        if lst[middle] == target:
            return middle

        # If the target is greater than the middle value,
        # eliminate the lower half of the search space.
        elif target > lst[middle]:
            low = middle + 1

        # Otherwise, eliminate the upper half.
        # Each iteration reduces the search space by about half.
        else:
            high = middle - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================

    print("\n=== SMALL DATASET TEST ===")

    small_list = [10, 20, 30, 40, 50]

    # 30 exists at index 2.
    print("Linear search for 30:", linear_search(small_list, 30))
    print("Binary search for 30:", binary_search(small_list, 30))

    # 60 does not exist, so both searches return -1.
    print("Linear search for 60:", linear_search(small_list, 60))
    print("Binary search for 60:", binary_search(small_list, 60))

    # ===============================
    # LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    large_list = list(range(1, 10001))

    # Search for a value near the end of the list.
    print("Linear search for 9999:", linear_search(large_list, 9999))
    print("Binary search for 9999:", binary_search(large_list, 9999))

    # Both algorithms return the same index.
    # However, linear search may have to examine almost every
    # element, while binary search repeatedly cuts the search
    # area in half. This makes binary search much more efficient
    # as the dataset becomes larger.

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: An empty list contains no values.
    # Both algorithms should return -1.
    empty_list = []

    print("Linear search empty list:",
          linear_search(empty_list, 10))
    print("Binary search empty list:",
          binary_search(empty_list, 10))

    # Edge case 2: Search a single-element list.
    # Since 5 is present, both searches return index 0.
    single_list = [5]

    print("Linear search single-element list:",
          linear_search(single_list, 5))
    print("Binary search single-element list:",
          binary_search(single_list, 5))


if __name__ == "__main__":
    main()