"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the value held by this node.
        self.value = value

        # A new node begins without any children.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # An empty BST does not have a root node yet.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.
        """

        # The recursive method determines where the new value belongs.
        # Values smaller than the current node move left, while values
        # larger than the current node move right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Implement recursive BST insertion.
        """

        # If an empty position is reached, create the new node here.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # If value equals node.value, nothing is inserted.
        # This implementation does not allow duplicate values.

        # Return the current node so the tree links remain connected.
        return node

    def search(self, value):
        """
        Search for a value in the BST.
        """

        # A BST can often search more efficiently than a linear list
        # because each comparison tells us which half of the remaining
        # tree can be ignored.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Implement recursive BST search.
        """

        # Reaching None means the value is not in the tree.
        if node is None:
            return False

        # If the current node contains the value, the search is complete.
        if value == node.value:
            return True

        # If the value is smaller, only search the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Otherwise, only search the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        Implement in-order traversal.
        """

        if node is not None:
            # First visit the left subtree, which contains smaller values.
            self._inorder_recursive(node.left, values)

            # Then visit the current node.
            values.append(node.value)

            # Finally visit the right subtree, which contains larger values.
            self._inorder_recursive(node.right, values)

            # Because a BST stores smaller values on the left and larger
            # values on the right, visiting left, node, right produces
            # the values in sorted order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================

    print("\n=== TREE CONSTRUCTION ===")

    tree = BST()

    # These values create nodes on both the left and right sides
    # of the root.
    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        tree.insert(value)

    print("Values inserted:", values)

    # BST searching is efficient because each comparison lets us
    # choose either the left or right subtree. The other subtree
    # does not need to be searched, reducing the search space.


    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================

    print("\n=== IN-ORDER TRAVERSAL ===")

    traversal = tree.inorder()

    print("In-order traversal:", traversal)

    # In-order traversal visits the left subtree first, then the
    # current node, and then the right subtree. Since smaller values
    # are stored on the left and larger values on the right, this
    # produces the values in sorted order.


    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # These values exist in the tree, so search returns True.
    print("Search for 30:", tree.search(30))
    print("Search for 70:", tree.search(70))

    # These values were never inserted, so search returns False.
    print("Search for 25:", tree.search(25))
    print("Search for 100:", tree.search(100))


    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    empty_tree = BST()

    # Traversing an empty tree returns an empty list because
    # there are no nodes to visit.
    print("Empty tree traversal:", empty_tree.inorder())

    # Searching an empty tree returns False because the root is None.
    print("Search empty tree for 50:", empty_tree.search(50))

    # Duplicate insertion edge case:
    # 50 already exists in the original tree. Because this BST only
    # inserts values that are smaller or larger, the duplicate is ignored.
    tree.insert(50)

    print("After attempting duplicate 50:", tree.inorder())


if __name__ == "__main__":
    main()