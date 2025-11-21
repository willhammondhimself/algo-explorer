"""Linked List specific challenges."""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.linked_list import LinkedList
from challenges.challenge_manager import Challenge


class FindMiddleNodeChallenge(Challenge):
    """
    Challenge: Find the middle node of a linked list in one pass.

    Goal: Use the slow/fast pointer technique to find middle element efficiently.
    """

    def __init__(self):
        """Initialize find middle node challenge."""
        super().__init__(
            name="Find Middle Node",
            description="Find the middle element of the list [1,2,3,4,5] using one pass (slow/fast pointers)",
            goal="Identify the middle element (should be 3)",
            hint="Use the find_middle() method which implements the slow/fast pointer technique."
        )
        self.found_middle = None

    def setup(self) -> LinkedList:
        """
        Create initial linked list for the challenge.

        Returns:
            LinkedList with values [1, 2, 3, 4, 5]
        """
        ll = LinkedList()
        for i in range(1, 6):
            ll.insert_at_tail(i)
        return ll

    def validate(self, linked_list: LinkedList) -> bool:
        """
        Validate if middle element was found correctly.

        Args:
            linked_list: Current linked list state

        Returns:
            True if middle element is 3
        """
        middle = linked_list.find_middle()
        self.found_middle = middle
        return middle == 3

    def get_solution_steps(self) -> str:
        """
        Get solution explanation.

        Returns:
            Solution steps
        """
        return """Solution:
1. Use two pointers: slow and fast
2. Initialize both to head
3. Move slow pointer one step at a time
4. Move fast pointer two steps at a time
5. When fast reaches the end, slow is at middle

For list [1,2,3,4,5]:
- Step 1: slow=1, fast=1
- Step 2: slow=2, fast=3
- Step 3: slow=3, fast=5
- Fast reached end, slow is at middle (3)

This technique requires only one pass through the list!
Time: O(n), Space: O(1)"""
