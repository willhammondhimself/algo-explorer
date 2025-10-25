"""Queue data structure implementation."""
import copy


class Queue:
    """
    Queue data structure with FIFO (First In First Out) behavior."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue.

        """
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self):
        """
        Return the front item without removing it.

        """
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def clear(self):
        """Remove all items from the queue."""
        self.items.clear()

    def to_list(self):
        """Return a copy of the queue as a list (front to rear)."""
        return copy.copy(self.items)

    def get_state(self):
        """
        Get the current state for serialization.        """
        return {"items": copy.deepcopy(self.items)}

    def set_state(self, state):
        """
        Restore the queue from a saved state.        """
        self.items = copy.deepcopy(state["items"])

    def __str__(self):
        """String representation of the queue."""
        return f"Queue({self.items})"

    def __repr__(self):
        """Detailed representation of the queue."""
        return f"Queue(items={self.items})"


class QueueFromStacks:
    """
    Queue implementation using two stacks.
    Used for challenge mode.
    """

    def __init__(self):
        """Initialize queue with two empty stacks."""
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue

    def enqueue(self, item):
        """Add item to queue using stack operations."""
        self.stack1.append(item)

    def dequeue(self):
        """Remove and return front item using stack operations."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()

    def is_empty(self):
        """Check if queue is empty."""
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self):
        """Return number of items in queue."""
        return len(self.stack1) + len(self.stack2)
