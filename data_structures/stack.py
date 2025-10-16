"""Stack data structure implementation."""
import copy


class Stack:
    """Basic stack using a list."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def clear(self):
        """Remove all items from the stack."""
        self.items.clear()

    def to_list(self):
        """Return a copy of the stack as a list."""
        return copy.copy(self.items)

    def get_state(self):
        """Get the current state for serialization."""
        return {"items": copy.deepcopy(self.items)}

    def set_state(self, state):
        """Restore the stack from a saved state."""
        self.items = copy.deepcopy(state["items"])

    def reverse_recursive(self):
        """Reverse the stack using recursion."""
        if not self.is_empty():
            temp = self.pop()
            self.reverse_recursive()
            self._insert_at_bottom(temp)

    def _insert_at_bottom(self, item):
        """Helper method to insert item at the bottom of the stack."""
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self._insert_at_bottom(item)
            self.push(temp)

    def __str__(self):
        """String representation of the stack."""
        return f"Stack({self.items})"

    def __repr__(self):
        """Detailed representation of the stack."""
        return f"Stack(items={self.items})"
