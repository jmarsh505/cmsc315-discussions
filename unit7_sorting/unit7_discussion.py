"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================
"""


def bubble_sort(lst):
    """
    Sorts a list using the Bubble Sort algorithm.
    """

    # Create a copy so the original list is not changed
    sorted_list = lst.copy()

    # Repeat through the list
    for i in range(len(sorted_list) - 1):

        # Track whether any swaps happened during this pass
        swapped = False

        # Compare neighboring values
        for j in range(len(sorted_list) - 1 - i):

            # Swap the values if they are in the wrong order
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )
                swapped = True

        # If no swaps happened, the list is already sorted
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    Sorts a list using the recursive Merge Sort algorithm.
    """

    # Base case: a list with 0 or 1 values is already sorted
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle of the list
    middle = len(lst) // 2

    # Divide the list into two halves
    left = lst[:middle]
    right = lst[middle:]

    # Recursively sort each half
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Merge the two sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Combines two sorted lists into one sorted list.
    """

    result = []

    # Indexes used to move through both lists
    i = 0
    j = 0

    # Compare values from the left and right lists
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any values remaining in the left list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any values remaining in the right list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # DATASET #1
    # ===============================

    print("\n=== DATASET #1 ===")

    dataset1 = [42, 17, 8, 63, 25, 91, 34]

    print("Original List:", dataset1)
    print("Bubble Sort:", bubble_sort(dataset1))
    print("Merge Sort:", merge_sort(dataset1))

    # ===============================
    # DATASET #2
    # ===============================

    print("\n=== DATASET #2 ===")

    dataset2 = [75, 12, 56, 3, 88, 29, 41, 19]

    print("Original List:", dataset2)
    print("Bubble Sort:", bubble_sort(dataset2))
    print("Merge Sort:", merge_sort(dataset2))

    # Compare the results from both algorithms
    if bubble_sort(dataset2) == merge_sort(dataset2):
        print("Both algorithms produced the same sorted result.")

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print("\nEmpty List:")
    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))
    print("Both algorithms return an empty list because there are no values to sort.")

    # Edge Case 2: List with duplicate values
    duplicate_list = [5, 2, 5, 1, 2, 8, 5]

    print("\nList With Duplicates:")
    print("Original:", duplicate_list)
    print("Bubble Sort:", bubble_sort(duplicate_list))
    print("Merge Sort:", merge_sort(duplicate_list))
    print("Duplicate values are kept and placed in their correct sorted positions.")


if __name__ == "__main__":
    main()