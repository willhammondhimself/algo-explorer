"""Comprehensive tests for Stack data structure."""
import pytest
from data_structures.stack import Stack


class TestStackBasicOperations:
    """Test basic stack operations."""

    def test_push_single_element(self):
        """Test pushing a single element onto the stack."""
        stack = Stack()
        stack.push(1)
        assert stack.size() == 1
        assert stack.peek() == 1

    def test_push_multiple_elements(self):
        """Test pushing multiple elements onto the stack."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.size() == 3
        assert stack.peek() == 3

    def test_pop_single_element(self):
        """Test popping a single element from the stack."""
        stack = Stack()
        stack.push(1)
        assert stack.pop() == 1
        assert stack.is_empty()

    def test_pop_multiple_elements_lifo_order(self):
        """Test that pop returns elements in LIFO order."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty()

    def test_peek_without_removal(self):
        """Test that peek returns top element without removing it."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert stack.size() == 2  # Size unchanged
        assert stack.peek() == 2  # Still same element


class TestStackEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_stack_initialization(self):
        """Test that a new stack is empty."""
        stack = Stack()
        assert stack.is_empty()
        assert stack.size() == 0

    def test_pop_from_empty_stack(self):
        """Test that popping from empty stack returns None."""
        stack = Stack()
        assert stack.pop() is None
        assert stack.is_empty()

    def test_peek_from_empty_stack(self):
        """Test that peeking at empty stack returns None."""
        stack = Stack()
        assert stack.peek() is None

    def test_single_element_stack(self):
        """Test operations on single-element stack."""
        stack = Stack()
        stack.push(42)
        assert not stack.is_empty()
        assert stack.size() == 1
        assert stack.peek() == 42
        assert stack.pop() == 42
        assert stack.is_empty()

    def test_push_pop_alternating(self):
        """Test alternating push and pop operations."""
        stack = Stack()
        stack.push(1)
        assert stack.pop() == 1
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.size() == 1


class TestStackUtilityMethods:
    """Test utility methods."""

    def test_clear_empty_stack(self):
        """Test clearing an empty stack."""
        stack = Stack()
        stack.clear()
        assert stack.is_empty()

    def test_clear_populated_stack(self):
        """Test clearing a populated stack."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.clear()
        assert stack.is_empty()
        assert stack.size() == 0

    def test_to_list_empty_stack(self):
        """Test converting empty stack to list."""
        stack = Stack()
        assert stack.to_list() == []

    def test_to_list_populated_stack(self):
        """Test converting populated stack to list (bottom to top)."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.to_list() == [1, 2, 3]

    def test_to_list_returns_copy(self):
        """Test that to_list returns a copy, not reference."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        lst = stack.to_list()
        lst.append(3)
        assert stack.size() == 2  # Stack unchanged


class TestStackStateManagement:
    """Test state serialization and restoration."""

    def test_get_state_empty_stack(self):
        """Test getting state from empty stack."""
        stack = Stack()
        state = stack.get_state()
        assert state == {"items": []}

    def test_get_state_populated_stack(self):
        """Test getting state from populated stack."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        state = stack.get_state()
        assert state == {"items": [1, 2, 3]}

    def test_set_state_restore(self):
        """Test restoring stack from saved state."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        state = stack.get_state()

        # Create new stack and restore
        new_stack = Stack()
        new_stack.set_state(state)
        assert new_stack.size() == 2
        assert new_stack.pop() == 2
        assert new_stack.pop() == 1

    def test_state_independence(self):
        """Test that state is deep copied (not referenced)."""
        stack = Stack()
        stack.push([1, 2, 3])
        state = stack.get_state()

        # Modify the state
        state["items"][0].append(4)

        # Original stack should be unchanged
        assert stack.peek() == [1, 2, 3]


class TestStackReverseRecursive:
    """Test recursive reversal operation."""

    def test_reverse_empty_stack(self):
        """Test reversing empty stack."""
        stack = Stack()
        stack.reverse_recursive()
        assert stack.is_empty()

    def test_reverse_single_element(self):
        """Test reversing single-element stack."""
        stack = Stack()
        stack.push(1)
        stack.reverse_recursive()
        assert stack.peek() == 1
        assert stack.size() == 1

    def test_reverse_multiple_elements(self):
        """Test reversing stack with multiple elements."""
        stack = Stack()
        for i in [1, 2, 3, 4, 5]:
            stack.push(i)

        stack.reverse_recursive()

        # After reversal, pop order should be 1, 2, 3, 4, 5
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3
        assert stack.pop() == 4
        assert stack.pop() == 5

    def test_reverse_twice_returns_original(self):
        """Test that reversing twice returns original order."""
        stack = Stack()
        original = [1, 2, 3, 4, 5]
        for item in original:
            stack.push(item)

        stack.reverse_recursive()
        stack.reverse_recursive()

        # Should be back to original
        assert stack.to_list() == original


class TestStackDataTypes:
    """Test stack with different data types."""

    def test_stack_with_strings(self):
        """Test stack with string elements."""
        stack = Stack()
        stack.push("hello")
        stack.push("world")
        assert stack.pop() == "world"
        assert stack.pop() == "hello"

    def test_stack_with_mixed_types(self):
        """Test stack with mixed data types."""
        stack = Stack()
        stack.push(1)
        stack.push("two")
        stack.push(3.0)
        stack.push([4, 5])
        assert stack.size() == 4
        assert stack.pop() == [4, 5]
        assert stack.pop() == 3.0

    def test_stack_with_none_values(self):
        """Test stack can store None as valid value."""
        stack = Stack()
        stack.push(1)
        stack.push(None)
        stack.push(3)
        assert stack.size() == 3
        assert stack.pop() == 3
        assert stack.pop() is None
        assert stack.pop() == 1


class TestStackStringRepresentation:
    """Test string representations."""

    def test_str_empty_stack(self):
        """Test __str__ for empty stack."""
        stack = Stack()
        assert str(stack) == "Stack([])"

    def test_str_populated_stack(self):
        """Test __str__ for populated stack."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert str(stack) == "Stack([1, 2])"

    def test_repr_stack(self):
        """Test __repr__ for stack."""
        stack = Stack()
        stack.push(1)
        assert repr(stack) == "Stack(items=[1])"
