"""Comprehensive tests for Queue data structure."""
import pytest
from data_structures.queue import Queue, QueueFromStacks


class TestQueueBasicOperations:
    """Test basic queue operations."""

    def test_enqueue_single_element(self):
        """Test enqueueing a single element."""
        queue = Queue()
        queue.enqueue(1)
        assert queue.size() == 1
        assert queue.front() == 1

    def test_enqueue_multiple_elements(self):
        """Test enqueueing multiple elements."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.size() == 3
        assert queue.front() == 1  # First element still at front

    def test_dequeue_single_element(self):
        """Test dequeueing a single element."""
        queue = Queue()
        queue.enqueue(1)
        assert queue.dequeue() == 1
        assert queue.is_empty()

    def test_dequeue_multiple_elements_fifo_order(self):
        """Test that dequeue returns elements in FIFO order."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty()

    def test_front_without_removal(self):
        """Test that front returns element without removing it."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.front() == 1
        assert queue.size() == 2  # Size unchanged
        assert queue.front() == 1  # Still same element


class TestQueueEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_queue_initialization(self):
        """Test that a new queue is empty."""
        queue = Queue()
        assert queue.is_empty()
        assert queue.size() == 0

    def test_dequeue_from_empty_queue(self):
        """Test that dequeueing from empty queue returns None."""
        queue = Queue()
        assert queue.dequeue() is None
        assert queue.is_empty()

    def test_front_from_empty_queue(self):
        """Test that checking front of empty queue returns None."""
        queue = Queue()
        assert queue.front() is None

    def test_single_element_queue(self):
        """Test operations on single-element queue."""
        queue = Queue()
        queue.enqueue(42)
        assert not queue.is_empty()
        assert queue.size() == 1
        assert queue.front() == 42
        assert queue.dequeue() == 42
        assert queue.is_empty()

    def test_enqueue_dequeue_alternating(self):
        """Test alternating enqueue and dequeue operations."""
        queue = Queue()
        queue.enqueue(1)
        assert queue.dequeue() == 1
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 2
        assert queue.size() == 1


class TestQueueUtilityMethods:
    """Test utility methods."""

    def test_clear_empty_queue(self):
        """Test clearing an empty queue."""
        queue = Queue()
        queue.clear()
        assert queue.is_empty()

    def test_clear_populated_queue(self):
        """Test clearing a populated queue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.clear()
        assert queue.is_empty()
        assert queue.size() == 0

    def test_to_list_empty_queue(self):
        """Test converting empty queue to list."""
        queue = Queue()
        assert queue.to_list() == []

    def test_to_list_populated_queue(self):
        """Test converting populated queue to list (front to rear)."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.to_list() == [1, 2, 3]

    def test_to_list_returns_copy(self):
        """Test that to_list returns a copy, not reference."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        lst = queue.to_list()
        lst.append(3)
        assert queue.size() == 2  # Queue unchanged


class TestQueueStateManagement:
    """Test state serialization and restoration."""

    def test_get_state_empty_queue(self):
        """Test getting state from empty queue."""
        queue = Queue()
        state = queue.get_state()
        assert state == {"items": []}

    def test_get_state_populated_queue(self):
        """Test getting state from populated queue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        state = queue.get_state()
        assert state == {"items": [1, 2, 3]}

    def test_set_state_restore(self):
        """Test restoring queue from saved state."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        state = queue.get_state()

        # Create new queue and restore
        new_queue = Queue()
        new_queue.set_state(state)
        assert new_queue.size() == 2
        assert new_queue.dequeue() == 1
        assert new_queue.dequeue() == 2

    def test_state_independence(self):
        """Test that state is deep copied (not referenced)."""
        queue = Queue()
        queue.enqueue([1, 2, 3])
        state = queue.get_state()

        # Modify the state
        state["items"][0].append(4)

        # Original queue should be unchanged
        assert queue.front() == [1, 2, 3]


class TestQueueDataTypes:
    """Test queue with different data types."""

    def test_queue_with_strings(self):
        """Test queue with string elements."""
        queue = Queue()
        queue.enqueue("first")
        queue.enqueue("second")
        assert queue.dequeue() == "first"
        assert queue.dequeue() == "second"

    def test_queue_with_mixed_types(self):
        """Test queue with mixed data types."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue("two")
        queue.enqueue(3.0)
        queue.enqueue([4, 5])
        assert queue.size() == 4
        assert queue.dequeue() == 1
        assert queue.dequeue() == "two"

    def test_queue_with_none_values(self):
        """Test queue can store None as valid value."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(None)
        queue.enqueue(3)
        assert queue.size() == 3
        assert queue.dequeue() == 1
        assert queue.dequeue() is None
        assert queue.dequeue() == 3


class TestQueueStringRepresentation:
    """Test string representations."""

    def test_str_empty_queue(self):
        """Test __str__ for empty queue."""
        queue = Queue()
        assert str(queue) == "Queue([])"

    def test_str_populated_queue(self):
        """Test __str__ for populated queue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert str(queue) == "Queue([1, 2])"

    def test_repr_queue(self):
        """Test __repr__ for queue."""
        queue = Queue()
        queue.enqueue(1)
        assert repr(queue) == "Queue(items=[1])"


class TestQueueFromStacks:
    """Test QueueFromStacks implementation (challenge mode)."""

    def test_queue_from_stacks_initialization(self):
        """Test QueueFromStacks initializes empty."""
        queue = QueueFromStacks()
        assert queue.is_empty()
        assert queue.size() == 0

    def test_queue_from_stacks_enqueue(self):
        """Test enqueue operation in QueueFromStacks."""
        queue = QueueFromStacks()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.size() == 3

    def test_queue_from_stacks_dequeue_fifo_order(self):
        """Test dequeue maintains FIFO order."""
        queue = QueueFromStacks()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty()

    def test_queue_from_stacks_dequeue_empty(self):
        """Test dequeueing from empty QueueFromStacks."""
        queue = QueueFromStacks()
        assert queue.dequeue() is None

    def test_queue_from_stacks_mixed_operations(self):
        """Test mixed enqueue/dequeue operations."""
        queue = QueueFromStacks()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        queue.enqueue(3)
        queue.enqueue(4)
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.size() == 1

    def test_queue_from_stacks_size_tracking(self):
        """Test size tracking across both stacks."""
        queue = QueueFromStacks()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.size() == 3
        queue.dequeue()
        assert queue.size() == 2
        queue.enqueue(4)
        assert queue.size() == 3

    def test_queue_from_stacks_stack_transfer(self):
        """Test that items transfer between stacks correctly."""
        queue = QueueFromStacks()
        # Add items
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # First dequeue triggers transfer from stack1 to stack2
        assert queue.dequeue() == 1

        # Add more items to stack1
        queue.enqueue(4)
        queue.enqueue(5)

        # Continue dequeueing - should get from stack2 first
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        # Then from stack1
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
        assert queue.is_empty()

    def test_queue_from_stacks_empty_after_operations(self):
        """Test is_empty after various operations."""
        queue = QueueFromStacks()
        assert queue.is_empty()
        queue.enqueue(1)
        assert not queue.is_empty()
        queue.dequeue()
        assert queue.is_empty()


class TestQueueFIFOProperty:
    """Test FIFO property maintenance."""

    def test_fifo_order_large_sequence(self):
        """Test FIFO order with larger sequence."""
        queue = Queue()
        for i in range(1, 11):
            queue.enqueue(i)

        for i in range(1, 11):
            assert queue.dequeue() == i

    def test_fifo_after_partial_dequeue(self):
        """Test FIFO order after partial dequeue."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        queue.dequeue()  # Remove 1

        queue.enqueue(4)
        queue.enqueue(5)

        # Should dequeue in order: 2, 3, 4, 5
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
