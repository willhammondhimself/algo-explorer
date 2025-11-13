"""Command pattern implementation for undo/redo functionality."""
from typing import Any, Callable, Optional
from abc import ABC, abstractmethod


class Command(ABC):
    """
    Abstract base class for all commands.
    Implements the Command pattern for undo/redo operations.
    """

    @abstractmethod
    def execute(self) -> Any:
        """Execute the command and return the result."""
        pass

    @abstractmethod
    def undo(self) -> None:
        """Undo the command, reverting to previous state."""
        pass

    @abstractmethod
    def get_description(self) -> str:
        """Get a description of the command."""
        pass


class DataStructureCommand(Command):
    """
    Command for data structure operations with state management.

    Attributes:
        data_structure: The data structure being modified
        operation: Function to execute
        undo_operation: Function to undo (optional)
        description: Command description
        prev_state: State before execution
        result: Result of execution
    """

    def __init__(self, data_structure: Any, operation: Callable,
                 undo_operation: Optional[Callable] = None,
                 description: str = "Operation"):
        """
        Initialize the command.

        Args:
            data_structure: Data structure to operate on
            operation: Function that performs the operation
            undo_operation: Optional function to undo
            description: Description of the command
        """
        self.data_structure = data_structure
        self.operation = operation
        self.undo_operation = undo_operation
        self.description = description
        self.prev_state = None
        self.result = None

    def execute(self) -> Any:
        """
        Execute the command.

        Returns:
            Result of the operation
        """
        # Save state before execution
        if hasattr(self.data_structure, 'get_state'):
            self.prev_state = self.data_structure.get_state()

        # Execute operation
        self.result = self.operation()
        return self.result

    def undo(self) -> None:
        """Undo the command by restoring previous state."""
        if self.undo_operation:
            self.undo_operation()
        elif self.prev_state and hasattr(self.data_structure, 'set_state'):
            self.data_structure.set_state(self.prev_state)

    def get_description(self) -> str:
        """Get command description."""
        return self.description


class CommandHistory:
    """
    Manages command history for undo/redo functionality.

    Attributes:
        history: List of executed commands
        current_index: Current position in history
        max_history: Maximum number of commands to keep
    """

    def __init__(self, max_history: int = 50):
        """
        Initialize command history.

        Args:
            max_history: Maximum commands to keep in history
        """
        self.history = []
        self.current_index = -1
        self.max_history = max_history

    def execute(self, command: Command) -> Any:
        """
        Execute a command and add to history.

        Args:
            command: Command to execute

        Returns:
            Result of command execution
        """
        # Remove any commands after current index (redo history)
        if self.current_index < len(self.history) - 1:
            self.history = self.history[:self.current_index + 1]

        # Execute command
        result = command.execute()

        # Add to history
        self.history.append(command)
        self.current_index += 1

        # Trim history if needed
        if len(self.history) > self.max_history:
            self.history.pop(0)
            self.current_index -= 1

        return result

    def undo(self) -> bool:
        """
        Undo the last command.

        Returns:
            True if undo was performed, False if nothing to undo
        """
        if not self.can_undo():
            return False

        command = self.history[self.current_index]
        command.undo()
        self.current_index -= 1
        return True

    def redo(self) -> bool:
        """
        Redo the last undone command.

        Returns:
            True if redo was performed, False if nothing to redo
        """
        if not self.can_redo():
            return False

        self.current_index += 1
        command = self.history[self.current_index]
        command.execute()
        return True

    def can_undo(self) -> bool:
        """Check if undo is available."""
        return self.current_index >= 0

    def can_redo(self) -> bool:
        """Check if redo is available."""
        return self.current_index < len(self.history) - 1

    def get_current_state(self) -> str:
        """
        Get description of current state.

        Returns:
            Description string
        """
        if self.current_index < 0:
            return "No operations"

        command = self.history[self.current_index]
        return command.get_description()

    def clear(self) -> None:
        """Clear all history."""
        self.history.clear()
        self.current_index = -1

    def get_history_size(self) -> int:
        """Get number of commands in history."""
        return len(self.history)
