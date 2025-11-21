"""Queue-specific challenges."""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.queue import Queue, QueueFromStacks
from challenges.challenge_manager import Challenge


class QueueFromStacksChallenge(Challenge):
    """
    Challenge: Implement a queue using two stacks.

    Goal: Understand how FIFO behavior can be achieved using two LIFO structures.
    """

    def __init__(self):
        """Initialize queue from stacks challenge."""
        super().__init__(
            name="Queue from Two Stacks",
            description="Implement queue operations using two stacks. Test by enqueuing [1,2,3] and dequeuing all.",
            goal="Dequeue operations should return elements in FIFO order: 1, 2, 3",
            hint="The QueueFromStacks class uses stack1 for enqueue and stack2 for dequeue."
        )
        self.expected_sequence = [1, 2, 3]
        self.dequeue_results = []

    def setup(self) -> QueueFromStacks:
        """
        Create initial queue from stacks.

        Returns:
            Empty QueueFromStacks instance
        """
        return QueueFromStacks()

    def validate(self, queue: QueueFromStacks) -> bool:
        """
        Validate queue behavior.

        Args:
            queue: QueueFromStacks instance

        Returns:
            True if operations maintain FIFO order
        """
        # This validation is manual - user needs to verify dequeue order
        # In the UI, we'll track dequeue operations
        return queue.is_empty() and len(self.dequeue_results) == 3

    def record_dequeue(self, value: any) -> None:
        """
        Record a dequeue operation for validation.

        Args:
            value: Dequeued value
        """
        self.dequeue_results.append(value)

    def check_sequence(self) -> bool:
        """
        Check if dequeued values are in correct order.

        Returns:
            True if sequence matches expected
        """
        return self.dequeue_results == self.expected_sequence

    def get_solution_steps(self) -> str:
        """
        Get solution explanation.

        Returns:
            Solution steps
        """
        return """Solution:
1. Enqueue 1, 2, 3 using the enqueue method
   - All values go into stack1
2. Dequeue the first element:
   - Transfer all from stack1 to stack2 (reversing order)
   - Pop from stack2 (returns 1)
3. Continue dequeuing:
   - Elements come from stack2 in correct FIFO order
   - Returns 2, then 3

Key insight: Moving elements between stacks reverses their order,
achieving FIFO behavior from LIFO structures."""
