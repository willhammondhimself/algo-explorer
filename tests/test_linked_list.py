"""Comprehensive tests for Linked List data structure."""
import pytest
from data_structures.linked_list import LinkedList, Node


class TestNodeBasics:
    """Test Node class."""

    def test_node_creation(self):
        """Test creating a node."""
        node = Node(5)
        assert node.data == 5
        assert node.next is None

    def test_node_str_representation(self):
        """Test node string representation."""
        node = Node(42)
        assert str(node) == "Node(42)"

    def test_node_repr(self):
        """Test node repr."""
        node = Node(10)
        assert repr(node) == "Node(data=10)"


class TestLinkedListInsertOperations:
    """Test insertion operations."""

    def test_insert_at_head_empty_list(self):
        """Test inserting at head of empty list."""
        ll = LinkedList()
        ll.insert_at_head(1)
        assert ll.size() == 1
        assert ll.to_list() == [1]

    def test_insert_at_head_multiple(self):
        """Test inserting multiple elements at head."""
        ll = LinkedList()
        ll.insert_at_head(1)
        ll.insert_at_head(2)
        ll.insert_at_head(3)
        assert ll.to_list() == [3, 2, 1]

    def test_insert_at_tail_empty_list(self):
        """Test inserting at tail of empty list."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        assert ll.size() == 1
        assert ll.to_list() == [1]

    def test_insert_at_tail_multiple(self):
        """Test inserting multiple elements at tail."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.to_list() == [1, 2, 3]

    def test_insert_at_position_beginning(self):
        """Test inserting at position 0."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        assert ll.insert_at_position(0, 0) is True
        assert ll.to_list() == [0, 1, 2]

    def test_insert_at_position_middle(self):
        """Test inserting in the middle."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(3)
        assert ll.insert_at_position(2, 1) is True
        assert ll.to_list() == [1, 2, 3]

    def test_insert_at_position_end(self):
        """Test inserting at the end."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        assert ll.insert_at_position(3, 2) is True
        assert ll.to_list() == [1, 2, 3]

    def test_insert_at_position_invalid_negative(self):
        """Test inserting at negative position."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        assert ll.insert_at_position(99, -1) is False
        assert ll.to_list() == [1]

    def test_insert_at_position_invalid_too_large(self):
        """Test inserting at position beyond list size."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        assert ll.insert_at_position(99, 5) is False
        assert ll.to_list() == [1]


class TestLinkedListDeleteOperations:
    """Test deletion operations."""

    def test_delete_from_empty_list(self):
        """Test deleting from empty list."""
        ll = LinkedList()
        assert ll.delete(1) is False

    def test_delete_head_element(self):
        """Test deleting head element."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.delete(1) is True
        assert ll.to_list() == [2, 3]

    def test_delete_middle_element(self):
        """Test deleting middle element."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.delete(2) is True
        assert ll.to_list() == [1, 3]

    def test_delete_tail_element(self):
        """Test deleting tail element."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.delete(3) is True
        assert ll.to_list() == [1, 2]

    def test_delete_nonexistent_element(self):
        """Test deleting element not in list."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        assert ll.delete(99) is False
        assert ll.to_list() == [1, 2]

    def test_delete_only_first_occurrence(self):
        """Test that delete removes only first occurrence."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(1)
        assert ll.delete(1) is True
        assert ll.to_list() == [2, 1]

    def test_delete_at_position_head(self):
        """Test deleting at position 0."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.delete_at_position(0) is True
        assert ll.to_list() == [2, 3]

    def test_delete_at_position_middle(self):
        """Test deleting at middle position."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.delete_at_position(1) is True
        assert ll.to_list() == [1, 3]

    def test_delete_at_position_tail(self):
        """Test deleting at last position."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.delete_at_position(2) is True
        assert ll.to_list() == [1, 2]

    def test_delete_at_position_invalid_negative(self):
        """Test deleting at negative position."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        assert ll.delete_at_position(-1) is False
        assert ll.to_list() == [1]

    def test_delete_at_position_invalid_too_large(self):
        """Test deleting at position beyond list size."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        assert ll.delete_at_position(5) is False
        assert ll.to_list() == [1]


class TestLinkedListSearchOperations:
    """Test search operations."""

    def test_search_empty_list(self):
        """Test searching in empty list."""
        ll = LinkedList()
        assert ll.search(1) is None

    def test_search_found_at_head(self):
        """Test searching for head element."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.search(1) == 0

    def test_search_found_at_middle(self):
        """Test searching for middle element."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.search(2) == 1

    def test_search_found_at_tail(self):
        """Test searching for tail element."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.search(3) == 2

    def test_search_not_found(self):
        """Test searching for nonexistent element."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        assert ll.search(99) is None

    def test_search_returns_first_occurrence(self):
        """Test search returns position of first occurrence."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(1)
        assert ll.search(1) == 0


class TestLinkedListFindMiddle:
    """Test find_middle operation (slow/fast pointer algorithm)."""

    def test_find_middle_empty_list(self):
        """Test finding middle of empty list."""
        ll = LinkedList()
        assert ll.find_middle() is None

    def test_find_middle_single_element(self):
        """Test finding middle of single-element list."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        assert ll.find_middle() == 1

    def test_find_middle_two_elements(self):
        """Test finding middle of two-element list."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        assert ll.find_middle() == 2

    def test_find_middle_odd_length(self):
        """Test finding middle of odd-length list."""
        ll = LinkedList()
        for i in [1, 2, 3, 4, 5]:
            ll.insert_at_tail(i)
        assert ll.find_middle() == 3

    def test_find_middle_even_length(self):
        """Test finding middle of even-length list."""
        ll = LinkedList()
        for i in [1, 2, 3, 4]:
            ll.insert_at_tail(i)
        # For even length, slow pointer stops at second middle
        assert ll.find_middle() == 3

    def test_find_middle_after_modifications(self):
        """Test find_middle after insertions and deletions."""
        ll = LinkedList()
        for i in [1, 2, 3, 4, 5]:
            ll.insert_at_tail(i)
        ll.delete(1)
        ll.delete(5)
        # Now list is [2, 3, 4]
        assert ll.find_middle() == 3


class TestLinkedListEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_list_initialization(self):
        """Test that new list is empty."""
        ll = LinkedList()
        assert ll.is_empty()
        assert ll.size() == 0

    def test_single_element_operations(self):
        """Test operations on single-element list."""
        ll = LinkedList()
        ll.insert_at_head(42)
        assert not ll.is_empty()
        assert ll.size() == 1
        assert ll.search(42) == 0
        assert ll.delete(42) is True
        assert ll.is_empty()

    def test_clear_empty_list(self):
        """Test clearing empty list."""
        ll = LinkedList()
        ll.clear()
        assert ll.is_empty()

    def test_clear_populated_list(self):
        """Test clearing populated list."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        ll.clear()
        assert ll.is_empty()
        assert ll.size() == 0


class TestLinkedListUtilityMethods:
    """Test utility methods."""

    def test_to_list_empty(self):
        """Test converting empty list."""
        ll = LinkedList()
        assert ll.to_list() == []

    def test_to_list_populated(self):
        """Test converting populated list."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert ll.to_list() == [1, 2, 3]

    def test_size_tracking(self):
        """Test that size is tracked correctly."""
        ll = LinkedList()
        assert ll.size() == 0
        ll.insert_at_head(1)
        assert ll.size() == 1
        ll.insert_at_tail(2)
        assert ll.size() == 2
        ll.delete(1)
        assert ll.size() == 1


class TestLinkedListStateManagement:
    """Test state serialization and restoration."""

    def test_get_state_empty_list(self):
        """Test getting state from empty list."""
        ll = LinkedList()
        state = ll.get_state()
        assert state == {"items": [], "size": 0}

    def test_get_state_populated_list(self):
        """Test getting state from populated list."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        state = ll.get_state()
        assert state == {"items": [1, 2, 3], "size": 3}

    def test_set_state_restore(self):
        """Test restoring list from saved state."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        state = ll.get_state()

        # Create new list and restore
        new_ll = LinkedList()
        new_ll.set_state(state)
        assert new_ll.size() == 3
        assert new_ll.to_list() == [1, 2, 3]


class TestLinkedListDataTypes:
    """Test list with different data types."""

    def test_list_with_strings(self):
        """Test list with string elements."""
        ll = LinkedList()
        ll.insert_at_tail("first")
        ll.insert_at_tail("second")
        assert ll.to_list() == ["first", "second"]

    def test_list_with_mixed_types(self):
        """Test list with mixed data types."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail("two")
        ll.insert_at_tail(3.0)
        assert ll.to_list() == [1, "two", 3.0]


class TestLinkedListStringRepresentation:
    """Test string representations."""

    def test_str_empty_list(self):
        """Test __str__ for empty list."""
        ll = LinkedList()
        assert str(ll) == "LinkedList()"

    def test_str_populated_list(self):
        """Test __str__ for populated list."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        ll.insert_at_tail(3)
        assert str(ll) == "LinkedList(1 -> 2 -> 3)"

    def test_repr_list(self):
        """Test __repr__ for list."""
        ll = LinkedList()
        ll.insert_at_tail(1)
        ll.insert_at_tail(2)
        assert repr(ll) == "LinkedList(size=2, items=[1, 2])"
