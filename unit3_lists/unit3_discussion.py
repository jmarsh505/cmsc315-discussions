"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.
    """

    #insert() places the new value at the specified index, shifting existing elements to the right.
    lst.insert(index, value)


    # Inserting near the beginning of a list can take more time because all subsequent elements need to be shifted.
    # Inserting near the end is generally faster since fewer elements need to be shifted.




def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.
    """

    #Validate the index before attempting to remove, pop() removes and returns the element at the specified index
    if 0 <= index < len(lst):
        return lst.pop(index)


    # If the index is invalid, return None to indicate that no element was removed.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.
    """

    #Linear search: iterate through the list sequentially to find the value.
    for index in range(len(lst)):
        if lst[index] == value:
            return index
    return -1  # Return -1 to indicate that the value was not found in the list.


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================

    print("\n=== INSERTION TESTS ===")

    #Create a list with several values.
    numbers = [10, 20, 30, 40, 50]
    print("Original list:", numbers)

    #Insert a value at the beginning of the list, shifting all existing values to the right.
    insert_at(numbers, 0, 5)
    print("List after inserting 5 at index 0:", numbers)

    #Insert a value in the middle of the list.
    insert_at(numbers, 3, 25)
    print("List after inserting 25 at index 3:", numbers)

    #Insert a value at the end of the list.
    insert_at(numbers, len(numbers), 60)
    print("List after inserting 60 at index", len(numbers), ":", numbers)



    # ===============================
    # DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")

    #Delete the first item
    removed = delete_at(numbers, 0)
    print("Removed item at index 0:", removed)
    print("List after deleting the first item:", numbers)

    #Delete an item from the middle of the list.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("Removed item from middle:", removed)
    print("List after deleting the middle item:", numbers)


    #Delete the last item in the list.
    removed = delete_at(numbers,len(numbers) - 1)
    print("Removed item at end:", removed)
    print("List after deleting the last item:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    #Search for a value that exists in the list.
    index = search_value(numbers, 30)
    if index != -1:
        print("Found value 30 at index:", index)
    else:
        print("Value 30 not found in the list.")

    #Search for a value that does not exist in the list.
    index = search_value(numbers, 99)
    if index != -1:
        print("Found value 99 at index:", index)
    else:
        print("Value 99 not found in the list.")

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    #Edge Case 1: Attempting to delete an item with an invalid index.
    removed = delete_at(numbers, -1)
    print("Deleting invalid index returned:", removed)


    #Edge Case 2: Attempting to insert at an invalid index.
    empty_list = []
    insert_at(empty_list, 0, 99)
    print("After inserting into an empty list:", empty_list)


    #Edge Case 3: Attempting to delete from an empty list.
    another_empty_list = []
    removed = delete_at(another_empty_list, 0)
    print("Deleting from an empty list returned:", removed)



if __name__ == "__main__":
    main()