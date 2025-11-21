"""Challenge manager - coordinates challenge mode across data structures."""
from typing import Dict, Any, Optional, Callable
from abc import ABC, abstractmethod


class Challenge(ABC):
    """
    Abstract base class for all challenges.

    Attributes:
        name: Challenge name
        description: Challenge description
        goal: Challenge goal
        hint: Hint for the challenge
    """

    def __init__(self, name: str, description: str, goal: str, hint: str = ""):
        """
        Initialize challenge.

        Args:
            name: Challenge name
            description: What the challenge asks
            goal: Success criteria
            hint: Optional hint
        """
        self.name = name
        self.description = description
        self.goal = goal
        self.hint = hint

    @abstractmethod
    def setup(self) -> Any:
        """
        Setup the challenge (create initial data structure).

        Returns:
            Initialized data structure
        """
        pass

    @abstractmethod
    def validate(self, data_structure: Any) -> bool:
        """
        Validate if the challenge is completed.

        Args:
            data_structure: Current state of data structure

        Returns:
            True if challenge is completed successfully
        """
        pass

    @abstractmethod
    def get_solution_steps(self) -> str:
        """
        Get explanation of solution steps.

        Returns:
            Solution explanation
        """
        pass


class ChallengeManager:
    """
    Manages challenges across all data structures.

    Attributes:
        challenges: Dictionary of available challenges by DS type
        active_challenge: Currently active challenge
        ds_type: Current data structure type
    """

    def __init__(self):
        """Initialize challenge manager."""
        self.challenges: Dict[str, list] = {
            'stack': [],
            'queue': [],
            'linked_list': [],
            'bst': []
        }
        self.active_challenge: Optional[Challenge] = None
        self.ds_type: Optional[str] = None

    def register_challenge(self, ds_type: str, challenge: Challenge) -> None:
        """
        Register a challenge for a data structure type.

        Args:
            ds_type: Data structure type ('stack', 'queue', 'linked_list', 'bst')
            challenge: Challenge instance
        """
        if ds_type in self.challenges:
            self.challenges[ds_type].append(challenge)

    def get_challenges(self, ds_type: str) -> list:
        """
        Get all challenges for a data structure type.

        Args:
            ds_type: Data structure type

        Returns:
            List of challenges
        """
        return self.challenges.get(ds_type, [])

    def start_challenge(self, ds_type: str, challenge_index: int) -> Optional[Any]:
        """
        Start a specific challenge.

        Args:
            ds_type: Data structure type
            challenge_index: Index of challenge to start

        Returns:
            Initialized data structure, or None if invalid
        """
        challenges = self.get_challenges(ds_type)
        if 0 <= challenge_index < len(challenges):
            self.active_challenge = challenges[challenge_index]
            self.ds_type = ds_type
            return self.active_challenge.setup()
        return None

    def validate_current(self, data_structure: Any) -> bool:
        """
        Validate the current active challenge.

        Args:
            data_structure: Current data structure state

        Returns:
            True if challenge is completed
        """
        if self.active_challenge:
            return self.active_challenge.validate(data_structure)
        return False

    def get_current_challenge_info(self) -> Optional[Dict[str, str]]:
        """
        Get information about current challenge.

        Returns:
            Dictionary with challenge info, or None if no active challenge
        """
        if self.active_challenge:
            return {
                'name': self.active_challenge.name,
                'description': self.active_challenge.description,
                'goal': self.active_challenge.goal,
                'hint': self.active_challenge.hint
            }
        return None

    def get_solution(self) -> Optional[str]:
        """
        Get solution steps for current challenge.

        Returns:
            Solution explanation, or None if no active challenge
        """
        if self.active_challenge:
            return self.active_challenge.get_solution_steps()
        return None

    def end_challenge(self) -> None:
        """End the current challenge."""
        self.active_challenge = None
        self.ds_type = None

    def is_challenge_active(self) -> bool:
        """Check if a challenge is currently active."""
        return self.active_challenge is not None
