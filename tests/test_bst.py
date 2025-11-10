"""Comprehensive tests for Binary Search Tree data structure."""
import pytest
from data_structures.bst import BinarySearchTree, TreeNode


class TestTreeNodeBasics:
    """Test TreeNode class."""

    def test_tree_node_creation(self):
        """Test creating a tree node."""
        node = TreeNode(5)
        assert node.data == 5
        assert node.left is None
        assert node.right is None

    def test_tree_node_str_representation(self):
        """Test tree node string representation."""
        node = TreeNode(42)
        assert str(node) == "TreeNode(42)"

    def test_tree_node_repr(self):
        """Test tree node repr."""
        node = TreeNode(10)
        assert repr(node) == "TreeNode(data=10)"


class TestBSTInsertOperations:
    """Test insertion operations."""

    def test_insert_into_empty_tree(self):
        """Test inserting into empty tree."""
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.size() == 1
        assert bst.root.data == 5

    def test_insert_smaller_value_goes_left(self):
        """Test that smaller values go to left subtree."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        assert bst.root.left.data == 3

    def test_insert_larger_value_goes_right(self):
        """Test that larger values go to right subtree."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(7)
        assert bst.root.right.data == 7

    def test_insert_multiple_values(self):
        """Test inserting multiple values."""
        bst = BinarySearchTree()
        values = [5, 3, 7, 1, 9]
        for val in values:
            bst.insert(val)
        assert bst.size() == 5
        assert bst.inorder_traversal() == [1, 3, 5, 7, 9]

    def test_insert_duplicate_value_ignored(self):
        """Test that duplicate values are not inserted."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(5)
        assert bst.size() == 1

    def test_insert_maintains_bst_property(self):
        """Test that BST property is maintained after inserts."""
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4, 6, 8]
        for val in values:
            bst.insert(val)
        # Inorder traversal should give sorted order
        assert bst.inorder_traversal() == sorted(values)


class TestBSTSearchOperations:
    """Test search operations."""

    def test_search_empty_tree(self):
        """Test searching in empty tree."""
        bst = BinarySearchTree()
        assert bst.search(5) is False

    def test_search_existing_root(self):
        """Test searching for root value."""
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.search(5) is True

    def test_search_existing_left_child(self):
        """Test searching for value in left subtree."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        assert bst.search(3) is True

    def test_search_existing_right_child(self):
        """Test searching for value in right subtree."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(7)
        assert bst.search(7) is True

    def test_search_nonexistent_value(self):
        """Test searching for nonexistent value."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        assert bst.search(10) is False

    def test_search_in_complex_tree(self):
        """Test searching in more complex tree."""
        bst = BinarySearchTree()
        values = [5, 3, 7, 1, 4, 6, 9]
        for val in values:
            bst.insert(val)
        assert bst.search(1) is True
        assert bst.search(9) is True
        assert bst.search(10) is False


class TestBSTDeleteOperations:
    """Test deletion operations."""

    def test_delete_from_empty_tree(self):
        """Test deleting from empty tree."""
        bst = BinarySearchTree()
        assert bst.delete(5) is False

    def test_delete_nonexistent_value(self):
        """Test deleting nonexistent value."""
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.delete(10) is False

    def test_delete_leaf_node(self):
        """Test deleting a leaf node."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        assert bst.delete(3) is True
        assert bst.search(3) is False
        assert bst.size() == 2

    def test_delete_node_with_one_left_child(self):
        """Test deleting node with only left child."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(2)
        assert bst.delete(3) is True
        assert bst.search(3) is False
        assert bst.search(2) is True
        assert bst.size() == 2

    def test_delete_node_with_one_right_child(self):
        """Test deleting node with only right child."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(4)
        assert bst.delete(3) is True
        assert bst.search(3) is False
        assert bst.search(4) is True
        assert bst.size() == 2

    def test_delete_node_with_two_children(self):
        """Test deleting node with two children."""
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4, 6, 8]
        for val in values:
            bst.insert(val)
        assert bst.delete(3) is True
        assert bst.search(3) is False
        # Tree should still maintain BST property
        inorder = bst.inorder_traversal()
        assert inorder == sorted(inorder)
        assert bst.size() == 6

    def test_delete_root_node(self):
        """Test deleting root node."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        assert bst.delete(5) is True
        assert bst.search(5) is False
        assert bst.size() == 2

    def test_delete_maintains_bst_property(self):
        """Test that BST property is maintained after deletion."""
        bst = BinarySearchTree()
        values = [5, 3, 7, 2, 4, 6, 8]
        for val in values:
            bst.insert(val)
        bst.delete(5)
        bst.delete(3)
        # Inorder should still be sorted
        inorder = bst.inorder_traversal()
        assert inorder == sorted(inorder)


class TestBSTTraversals:
    """Test tree traversal operations."""

    def test_inorder_empty_tree(self):
        """Test inorder traversal of empty tree."""
        bst = BinarySearchTree()
        assert bst.inorder_traversal() == []

    def test_inorder_single_node(self):
        """Test inorder traversal of single-node tree."""
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.inorder_traversal() == [5]

    def test_inorder_multiple_nodes(self):
        """Test inorder traversal gives sorted order."""
        bst = BinarySearchTree()
        values = [5, 3, 7, 1, 4, 6, 9]
        for val in values:
            bst.insert(val)
        assert bst.inorder_traversal() == [1, 3, 4, 5, 6, 7, 9]

    def test_preorder_empty_tree(self):
        """Test preorder traversal of empty tree."""
        bst = BinarySearchTree()
        assert bst.preorder_traversal() == []

    def test_preorder_single_node(self):
        """Test preorder traversal of single-node tree."""
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.preorder_traversal() == [5]

    def test_preorder_multiple_nodes(self):
        """Test preorder traversal (root, left, right)."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        bst.insert(4)
        assert bst.preorder_traversal() == [5, 3, 2, 4, 7]

    def test_postorder_empty_tree(self):
        """Test postorder traversal of empty tree."""
        bst = BinarySearchTree()
        assert bst.postorder_traversal() == []

    def test_postorder_single_node(self):
        """Test postorder traversal of single-node tree."""
        bst = BinarySearchTree()
        bst.insert(5)
        assert bst.postorder_traversal() == [5]

    def test_postorder_multiple_nodes(self):
        """Test postorder traversal (left, right, root)."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        bst.insert(4)
        assert bst.postorder_traversal() == [2, 4, 3, 7, 5]


class TestBSTBalancedBuild:
    """Test building balanced tree from sorted array."""

    def test_build_balanced_empty_array(self):
        """Test building balanced tree from empty array."""
        bst = BinarySearchTree.build_balanced_from_sorted([])
        assert bst.is_empty()
        assert bst.size() == 0

    def test_build_balanced_single_element(self):
        """Test building balanced tree from single element."""
        bst = BinarySearchTree.build_balanced_from_sorted([5])
        assert bst.size() == 1
        assert bst.root.data == 5

    def test_build_balanced_odd_elements(self):
        """Test building balanced tree from odd number of elements."""
        bst = BinarySearchTree.build_balanced_from_sorted([1, 2, 3, 4, 5, 6, 7])
        assert bst.size() == 7
        assert bst.root.data == 4  # Middle element becomes root
        assert bst.inorder_traversal() == [1, 2, 3, 4, 5, 6, 7]

    def test_build_balanced_even_elements(self):
        """Test building balanced tree from even number of elements."""
        bst = BinarySearchTree.build_balanced_from_sorted([1, 2, 3, 4, 5, 6])
        assert bst.size() == 6
        # Middle (rounded down) becomes root
        assert bst.inorder_traversal() == [1, 2, 3, 4, 5, 6]

    def test_build_balanced_maintains_bst_property(self):
        """Test that balanced tree maintains BST property."""
        bst = BinarySearchTree.build_balanced_from_sorted([1, 2, 3, 4, 5])
        inorder = bst.inorder_traversal()
        assert inorder == sorted(inorder)

    def test_build_balanced_structure(self):
        """Test that built tree has balanced structure."""
        bst = BinarySearchTree.build_balanced_from_sorted([1, 2, 3, 4, 5, 6, 7])
        # Root should be middle element
        assert bst.root.data == 4
        # Left and right subtrees should exist
        assert bst.root.left is not None
        assert bst.root.right is not None


class TestBSTEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_tree_initialization(self):
        """Test that new tree is empty."""
        bst = BinarySearchTree()
        assert bst.is_empty()
        assert bst.size() == 0

    def test_clear_empty_tree(self):
        """Test clearing empty tree."""
        bst = BinarySearchTree()
        bst.clear()
        assert bst.is_empty()

    def test_clear_populated_tree(self):
        """Test clearing populated tree."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.clear()
        assert bst.is_empty()
        assert bst.size() == 0

    def test_single_node_tree_operations(self):
        """Test operations on single-node tree."""
        bst = BinarySearchTree()
        bst.insert(5)
        assert not bst.is_empty()
        assert bst.size() == 1
        assert bst.search(5) is True
        assert bst.delete(5) is True
        assert bst.is_empty()


class TestBSTStateManagement:
    """Test state serialization and restoration."""

    def test_get_state_empty_tree(self):
        """Test getting state from empty tree."""
        bst = BinarySearchTree()
        state = bst.get_state()
        assert state == {"items": [], "size": 0}

    def test_get_state_populated_tree(self):
        """Test getting state from populated tree."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        state = bst.get_state()
        assert state["size"] == 3
        assert len(state["items"]) == 3

    def test_set_state_restore(self):
        """Test restoring tree from saved state."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        state = bst.get_state()

        # Create new tree and restore
        new_bst = BinarySearchTree()
        new_bst.set_state(state)
        assert new_bst.size() == 4
        assert new_bst.search(5) is True
        assert new_bst.search(3) is True
        assert new_bst.search(7) is True
        assert new_bst.search(1) is True


class TestBSTSizeTracking:
    """Test size tracking."""

    def test_size_after_insertions(self):
        """Test size tracking during insertions."""
        bst = BinarySearchTree()
        assert bst.size() == 0
        bst.insert(5)
        assert bst.size() == 1
        bst.insert(3)
        assert bst.size() == 2
        bst.insert(7)
        assert bst.size() == 3

    def test_size_after_deletions(self):
        """Test size tracking during deletions."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        assert bst.size() == 3
        bst.delete(3)
        assert bst.size() == 2
        bst.delete(7)
        assert bst.size() == 1

    def test_size_with_duplicate_insert_attempts(self):
        """Test that size doesn't increase on duplicate inserts."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(5)
        bst.insert(5)
        assert bst.size() == 1


class TestBSTStringRepresentation:
    """Test string representations."""

    def test_str_empty_tree(self):
        """Test __str__ for empty tree."""
        bst = BinarySearchTree()
        assert str(bst) == "BST(inorder=[])"

    def test_str_populated_tree(self):
        """Test __str__ for populated tree."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        assert str(bst) == "BST(inorder=[3, 5, 7])"

    def test_repr_tree(self):
        """Test __repr__ for tree."""
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        assert repr(bst) == "BinarySearchTree(size=2, inorder=[3, 5])"


class TestBSTPropertyValidation:
    """Test that BST property is always maintained."""

    def test_bst_property_after_random_operations(self):
        """Test BST property maintained after various operations."""
        bst = BinarySearchTree()
        operations = [
            ('insert', 5),
            ('insert', 3),
            ('insert', 7),
            ('insert', 1),
            ('insert', 9),
            ('delete', 3),
            ('insert', 4),
            ('delete', 5),
        ]

        for op, val in operations:
            if op == 'insert':
                bst.insert(val)
            elif op == 'delete':
                bst.delete(val)

        # Inorder should always be sorted (BST property)
        inorder = bst.inorder_traversal()
        assert inorder == sorted(inorder)
