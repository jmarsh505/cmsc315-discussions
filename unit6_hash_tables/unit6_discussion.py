"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================

    # A Python dictionary behaves like a hash table because it stores
    # information as key-value pairs. Python uses the key's hash value
    # to efficiently determine where the associated value is stored.
    student_scores = {}

    # Add five key-value pairs to the dictionary.
    student_scores["Alice"] = 92
    student_scores["Bob"] = 85
    student_scores["Charlie"] = 78
    student_scores["David"] = 95
    student_scores["Emma"] = 88

    print("\n=== INSERT OPERATIONS ===")
    print("Dictionary after inserting five students:")
    print(student_scores)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================

    print("\n=== LOOKUP OPERATIONS ===")

    # A value can be retrieved by using its key.
    # Dictionaries make lookups efficient because Python uses the
    # hash of the key to locate its associated value.
    print("Alice's score:", student_scores["Alice"])
    print("David's score:", student_scores["David"])

    # ===============================
    # UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:")
    print(student_scores)

    # Assigning a new value to an existing key replaces the old value.
    # It does not create a second "Bob" key.
    student_scores["Bob"] = 90

    print("After updating Bob's score:")
    print(student_scores)

    # ===============================
    # DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:")
    print(student_scores)

    # The del statement removes the key and its associated value
    # from the dictionary.
    del student_scores["Charlie"]

    print("After deleting Charlie:")
    print(student_scores)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Looking up a missing key.
    # The get() method safely returns None instead of causing an error
    # when the requested key does not exist.
    missing_score = student_scores.get("Frank")
    print("Looking up Frank:", missing_score)

    # Edge Case 2: Safely deleting a missing key.
    # Checking whether the key exists prevents a KeyError.
    if "George" in student_scores:
        del student_scores["George"]
    else:
        print("George was not found, so nothing was deleted.")

    print("\nFinal dictionary:")
    print(student_scores)


if __name__ == "__main__":
    main()