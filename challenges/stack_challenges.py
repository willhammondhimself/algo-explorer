"""Stack-specific challenges."""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.stack import Stack
from challenges.challenge_manager import Challenge


class ReverseStackChallenge(Challenge):
    """
    Challenge: Reverse a stack using recursion.

    Goal: Given a stack [1, 2, 3, 4, 5] (bottom to top),
          reverse it to [5, 4, 3, 2, 1] using the recursive method.
    """

    def __init__(self):
        """Initialize reverse stack challenge."""
        super().__init__(
            name="Reverse the Stack",
            description="Reverse a stack using recursion. Initial stack: [1, 2, 3, 4, 5] (bottom to top)",
            goal="The stack should become [5, 4, 3, 2, 1] (bottom to top)",
            hint="Use the reverse_recursive() method on the stack instance."
        )

    def setup(self) -> Stack:
        """
        Create initial stack for the challenge.

        Returns:
            Stack with values [1, 2, 3, 4, 5]
        """
        stack = Stack()
        for i in range(1, 6):
            stack.push(i)
        return stack

    def validate(self, stack: Stack) -> bool:
        """
        Validate if stack is reversed correctly.

        Args:
            stack: Current stack state

        Returns:
            True if stack is [5, 4, 3, 2, 1]
        """
        expected = [5, 4, 3, 2, 1]
        actual = stack.to_list()
        return actual == expected

    def get_solution_steps(self) -> str:
        """
        Get solution explanation.

        Returns:
            Solution steps
        """
        return """Solution:
1. Click 'Reverse Stack' button (or call reverse_recursive() method)
2. The recursive algorithm works by:
   - Popping each element
   - Recursively reversing the remaining stack
   - Inserting the popped element at the bottom
3. This demonstrates recursion with a call stack visualization

Expected result: Stack transforms from [1,2,3,4,5] to [5,4,3,2,1]"""
