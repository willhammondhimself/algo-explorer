"""BST specific challenges."""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.bst import BinarySearchTree
from challenges.challenge_manager import Challenge


class BuildBalancedBSTChallenge(Challenge):
    """
    Challenge: Build a balanced BST from a sorted array.

    Goal: Given sorted array [1,2,3,4,5,6,7], build a balanced BST.
    """
    # TODO: add step-by-step visualization showing how the tree is built
    # currently just shows final result

    def __init__(self):
        """Initialize balanced BST challenge."""
        super().__init__(
            name="Build Balanced BST",
            description="Build a balanced BST from sorted array [1,2,3,4,5,6,7]",
            goal="Create a balanced tree with minimal height",
            hint="Use build_balanced_from_sorted() static method with the sorted array."
        )
        self.sorted_array = [1, 2, 3, 4, 5, 6, 7]

    def setup(self) -> BinarySearchTree:
        """
        Create initial empty BST.

        Returns:
            Empty BinarySearchTree
        """
        return BinarySearchTree()

    def validate(self, bst: BinarySearchTree) -> bool:
        """
        Validate if BST is balanced and contains correct elements.

        Args:
            bst: Current BST state

        Returns:
            True if BST is balanced with correct elements
        """
        # Check if all elements are present
        inorder = bst.inorder_traversal()
        if sorted(inorder) != self.sorted_array:
            return False

        # Check if tree is balanced (height difference check)
        if not bst.root:
            return False

        # For a balanced tree from [1,2,3,4,5,6,7], root should be 4
        if bst.root.data != 4:
            return False

        # Verify structure
        return self._is_balanced(bst.root)

    def _is_balanced(self, node) -> bool:
        """
        Check if tree is balanced.

        Args:
            node: Root node

        Returns:
            True if balanced
        """
        def get_height(n):
            if n is None:
                return 0
            left_height = get_height(n.left)
            right_height = get_height(n.right)
            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return get_height(node) != -1

    def get_solution_steps(self) -> str:
        """
        Get solution explanation.

        Returns:
            Solution steps
        """
        return """Solution:
1. Use the middle element of sorted array as root
2. Recursively build left subtree from left half
3. Recursively build right subtree from right half

For array [1,2,3,4,5,6,7]:
- Middle = 4 (root)
- Left half [1,2,3]: middle = 2 (left child of 4)
  - Left of 2: 1
  - Right of 2: 3
- Right half [5,6,7]: middle = 6 (right child of 4)
  - Left of 6: 5
  - Right of 6: 7

Result: Balanced tree with height = 3
        4
       / \\
      2   6
     / \\ / \\
    1  3 5  7

Use: BinarySearchTree.build_balanced_from_sorted([1,2,3,4,5,6,7])"""
