"""Main window - primary application interface."""
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                            QTabWidget, QStatusBar, QMessageBox, QAction,
                            QMenuBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.linked_list import LinkedList
from data_structures.bst import BinarySearchTree

from visuals.stack_visualizer import StackVisualizer
from visuals.queue_visualizer import QueueVisualizer
from visuals.linked_list_visualizer import LinkedListVisualizer
from visuals.bst_visualizer import BSTVisualizer

from challenges.challenge_manager import ChallengeManager
from challenges.stack_challenges import ReverseStackChallenge
from challenges.queue_challenges import QueueFromStacksChallenge
from challenges.linked_list_challenges import FindMiddleNodeChallenge
from challenges.bst_challenges import BuildBalancedBSTChallenge

from ui.animation_canvas import AnimationCanvas
from ui.control_panel import ControlPanel
from ui.commands import CommandHistory, DataStructureCommand


class DSTab(QWidget):
    """
    Tab for a single data structure.

    Combines canvas, visualizer, and control panel.
    """

    def __init__(self, ds_type: str, parent=None, main_window=None):
        """
        Initialize data structure tab.

        Args:
            ds_type: Type of data structure
            parent: Parent widget
            main_window: Reference to main window for challenge mode
        """
        super().__init__(parent)
        self.ds_type = ds_type
        self.main_window = main_window
        self.command_history = CommandHistory()

        if ds_type == 'stack':
            self.data_structure = Stack()
        elif ds_type == 'queue':
            self.data_structure = Queue()
        elif ds_type == 'linked_list':
            self.data_structure = LinkedList()
        elif ds_type == 'bst':
            self.data_structure = BinarySearchTree()

        self.canvas = AnimationCanvas(self)
        self.control_panel = ControlPanel(ds_type, self)

        if ds_type == 'stack':
            self.visualizer = StackVisualizer(self.canvas.get_scene())
        elif ds_type == 'queue':
            self.visualizer = QueueVisualizer(self.canvas.get_scene())
        elif ds_type == 'linked_list':
            self.visualizer = LinkedListVisualizer(self.canvas.get_scene())
        elif ds_type == 'bst':
            self.visualizer = BSTVisualizer(self.canvas.get_scene())

        self.control_panel.operation_requested.connect(self.handle_operation)

        layout = QHBoxLayout()
        layout.addWidget(self.canvas, stretch=3)
        layout.addWidget(self.control_panel, stretch=1)
        self.setLayout(layout)

        self.visualizer.draw(self.data_structure)

    def handle_operation(self, operation: str, value) -> None:
        """
        Handle operation request from control panel.

        Args:
            operation: Operation name
            value: Operation value (if any)
        """
        try:
            if operation == 'clear':
                self.execute_clear()
            elif operation == 'push':
                self.execute_push(value)
            elif operation == 'pop':
                self.execute_pop()
            elif operation == 'peek':
                self.execute_peek()
            elif operation == 'reverse':
                self.execute_reverse()
            elif operation == 'enqueue':
                self.execute_enqueue(value)
            elif operation == 'dequeue':
                self.execute_dequeue()
            elif operation == 'front':
                self.execute_front()
            elif operation == 'insert_head':
                self.execute_insert_head(value)
            elif operation == 'insert_tail':
                self.execute_insert_tail(value)
            elif operation == 'delete':
                self.execute_delete(value)
            elif operation == 'search':
                self.execute_search(value)
            elif operation == 'find_middle':
                self.execute_find_middle()
            elif operation == 'insert':
                self.execute_insert(value)
            elif operation == 'inorder':
                self.execute_traversal('inorder')
            elif operation == 'preorder':
                self.execute_traversal('preorder')
            elif operation == 'postorder':
                self.execute_traversal('postorder')
            elif operation.startswith('start_challenge'):
                if self.main_window:
                    self.main_window.start_challenge(self.ds_type)
            elif operation == 'validate_challenge':
                if self.main_window:
                    self.main_window.validate_challenge()
            elif operation == 'show_hint':
                if self.main_window:
                    self.main_window.show_hint()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Operation failed: {str(e)}")

    # Stack operations
    def execute_push(self, value) -> None:
        """Execute push operation."""
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.push(value),
            description=f"Push {value}"
        )
        self.command_history.execute(cmd)
        self.visualizer.animate_insert(self.data_structure, value)
        self.update_status(f"Pushed {value}")

    def execute_pop(self) -> None:
        """Execute pop operation."""
        value = self.data_structure.peek()
        if value is None:
            QMessageBox.information(self, "Info", "Stack is empty")
            return
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.pop(),
            description="Pop"
        )
        result = self.command_history.execute(cmd)
        self.visualizer.animate_delete(self.data_structure, result)
        self.update_status(f"Popped {result}")

    def execute_peek(self) -> None:
        """Execute peek operation."""
        value = self.data_structure.peek()
        if value is None:
            QMessageBox.information(self, "Info", "Stack is empty")
        else:
            QMessageBox.information(self, "Peek", f"Top value: {value}")

    def execute_reverse(self) -> None:
        """Execute reverse stack operation."""
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.reverse_recursive(),
            description="Reverse stack"
        )
        self.command_history.execute(cmd)
        self.visualizer.draw(self.data_structure)
        self.update_status("Stack reversed")

    # Queue operations
    def execute_enqueue(self, value) -> None:
        """Execute enqueue operation."""
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.enqueue(value),
            description=f"Enqueue {value}"
        )
        self.command_history.execute(cmd)
        self.visualizer.animate_insert(self.data_structure, value)
        self.update_status(f"Enqueued {value}")

    def execute_dequeue(self) -> None:
        """Execute dequeue operation."""
        value = self.data_structure.front()
        if value is None:
            QMessageBox.information(self, "Info", "Queue is empty")
            return
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.dequeue(),
            description="Dequeue"
        )
        result = self.command_history.execute(cmd)
        self.visualizer.animate_delete(self.data_structure, result)
        self.update_status(f"Dequeued {result}")

    def execute_front(self) -> None:
        """Execute front operation."""
        value = self.data_structure.front()
        if value is None:
            QMessageBox.information(self, "Info", "Queue is empty")
        else:
            QMessageBox.information(self, "Front", f"Front value: {value}")

    # Linked List operations
    def execute_insert_head(self, value) -> None:
        """Execute insert at head operation."""
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.insert_at_head(value),
            description=f"Insert {value} at head"
        )
        self.command_history.execute(cmd)
        self.visualizer.animate_insert(self.data_structure, value, position=0)
        self.update_status(f"Inserted {value} at head")

    def execute_insert_tail(self, value) -> None:
        """Execute insert at tail operation."""
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.insert_at_tail(value),
            description=f"Insert {value} at tail"
        )
        self.command_history.execute(cmd)
        self.visualizer.draw(self.data_structure)
        self.update_status(f"Inserted {value} at tail")

    def execute_delete(self, value) -> None:
        """Execute delete operation."""
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.delete(value),
            description=f"Delete {value}"
        )
        result = self.command_history.execute(cmd)
        if result:
            self.visualizer.animate_delete(self.data_structure, value)
            self.update_status(f"Deleted {value}")
        else:
            QMessageBox.information(self, "Info", f"Value {value} not found")

    def execute_search(self, value) -> None:
        """Execute search operation."""
        self.visualizer.animate_search(self.data_structure, value)
        result = self.data_structure.search(value)
        if result is not None:
            self.update_status(f"Found {value} at position {result}")
        else:
            self.update_status(f"Value {value} not found")

    def execute_find_middle(self) -> None:
        """Execute find middle operation."""
        middle = self.data_structure.find_middle()
        if middle is not None:
            QMessageBox.information(self, "Middle Element", f"Middle value: {middle}")
            self.update_status(f"Middle element: {middle}")
        else:
            QMessageBox.information(self, "Info", "List is empty")

    # BST operations
    def execute_insert(self, value) -> None:
        """Execute BST insert operation."""
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.insert(value),
            description=f"Insert {value}"
        )
        self.command_history.execute(cmd)
        self.visualizer.animate_insert(self.data_structure, value)
        self.update_status(f"Inserted {value}")

    def execute_traversal(self, traversal_type: str) -> None:
        """Execute tree traversal."""
        self.visualizer.draw_traversal(self.data_structure, traversal_type)
        self.update_status(f"{traversal_type.capitalize()} traversal displayed")

    # Common operations
    def execute_clear(self) -> None:
        """Execute clear operation."""
        cmd = DataStructureCommand(
            self.data_structure,
            lambda: self.data_structure.clear(),
            description="Clear all"
        )
        self.command_history.execute(cmd)
        self.visualizer.draw(self.data_structure)
        self.update_status("Cleared all elements")

    def undo(self) -> None:
        """Undo last operation."""
        if self.command_history.undo():
            self.visualizer.draw(self.data_structure)
            self.update_status("Undo successful")
        else:
            QMessageBox.information(self, "Info", "Nothing to undo")

    def redo(self) -> None:
        """Redo last undone operation."""
        if self.command_history.redo():
            self.visualizer.draw(self.data_structure)
            self.update_status("Redo successful")
        else:
            QMessageBox.information(self, "Info", "Nothing to redo")

    def update_status(self, message: str) -> None:
        """Update status bar message."""
        main_window = self.parent().parent()
        if hasattr(main_window, 'statusBar'):
            main_window.statusBar().showMessage(message, 3000)


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        """Initialize main window."""
        super().__init__()
        self.setWindowTitle("Algo Explorer - Visual Data Structures Playground")
        self.setGeometry(100, 100, 1200, 800)

        self.challenge_manager = ChallengeManager()
        self._register_challenges()

        self.tabs = QTabWidget()
        self.stack_tab = DSTab('stack', main_window=self)
        self.queue_tab = DSTab('queue', main_window=self)
        self.linked_list_tab = DSTab('linked_list', main_window=self)
        self.bst_tab = DSTab('bst', main_window=self)

        self.tabs.addTab(self.stack_tab, "Stack")
        self.tabs.addTab(self.queue_tab, "Queue")
        self.tabs.addTab(self.linked_list_tab, "Linked List")
        self.tabs.addTab(self.bst_tab, "Binary Search Tree")

        self.setCentralWidget(self.tabs)

        self._create_menu_bar()
        self.statusBar().showMessage("Ready")

    def _register_challenges(self) -> None:
        """Register all challenges."""
        self.challenge_manager.register_challenge('stack', ReverseStackChallenge())
        self.challenge_manager.register_challenge('queue', QueueFromStacksChallenge())
        self.challenge_manager.register_challenge('linked_list', FindMiddleNodeChallenge())
        self.challenge_manager.register_challenge('bst', BuildBalancedBSTChallenge())

    def _create_menu_bar(self) -> None:
        """Create application menu bar."""
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Edit menu
        edit_menu = menubar.addMenu("Edit")

        undo_action = QAction("Undo", self)
        undo_action.setShortcut(QKeySequence.Undo)
        undo_action.triggered.connect(self.undo_current)
        edit_menu.addAction(undo_action)

        redo_action = QAction("Redo", self)
        redo_action.setShortcut(QKeySequence.Redo)
        redo_action.triggered.connect(self.redo_current)
        edit_menu.addAction(redo_action)

        # Help menu
        help_menu = menubar.addMenu("Help")

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def undo_current(self) -> None:
        """Undo operation in current tab."""
        current_tab = self.tabs.currentWidget()
        if isinstance(current_tab, DSTab):
            current_tab.undo()

    def redo_current(self) -> None:
        """Redo operation in current tab."""
        current_tab = self.tabs.currentWidget()
        if isinstance(current_tab, DSTab):
            current_tab.redo()

    def start_challenge(self, ds_type: str) -> None:
        """Start challenge for current data structure."""
        challenges = self.challenge_manager.get_challenges(ds_type)
        if not challenges:
            QMessageBox.information(self, "Info", "No challenges available for this data structure")
            return

        # For now, start first challenge (can be expanded to choose)
        ds = self.challenge_manager.start_challenge(ds_type, 0)

        # Get current tab and replace data structure
        current_tab = self.tabs.currentWidget()
        if isinstance(current_tab, DSTab):
            current_tab.data_structure = ds
            current_tab.visualizer.draw(ds)
            current_tab.control_panel.enable_challenge_mode(True)

            # Show challenge info
            info = self.challenge_manager.get_current_challenge_info()
            QMessageBox.information(
                self,
                info['name'],
                f"{info['description']}\n\nGoal: {info['goal']}"
            )
            self.statusBar().showMessage(f"Challenge started: {info['name']}")

    def validate_challenge(self) -> None:
        """Validate current challenge."""
        if not self.challenge_manager.is_challenge_active():
            return

        current_tab = self.tabs.currentWidget()
        if isinstance(current_tab, DSTab):
            is_valid = self.challenge_manager.validate_current(current_tab.data_structure)

            if is_valid:
                QMessageBox.information(
                    self,
                    "Success!",
                    "Congratulations! You've completed the challenge successfully!"
                )
                current_tab.control_panel.enable_challenge_mode(False)
                self.challenge_manager.end_challenge()
            else:
                QMessageBox.warning(
                    self,
                    "Not Yet",
                    "The solution is not correct yet. Try again or click 'Show Hint'."
                )

    def show_hint(self) -> None:
        """Show hint for current challenge."""
        if not self.challenge_manager.is_challenge_active():
            return

        solution = self.challenge_manager.get_solution()
        QMessageBox.information(self, "Solution Steps", solution)

    def show_about(self) -> None:
        """Show about dialog."""
        QMessageBox.about(
            self,
            "About Algo Explorer",
            """Algo Explorer - Visual Data Structures Playground

A Python GUI application for visualizing and learning data structures.

Features:
- Interactive visualizations for Stack, Queue, Linked List, and BST
- Step-through animations for all operations
- Recursion visualization with call stack
- Challenge mode with built-in problems
- Undo/Redo support

Built with PyQt5 and Python."""
        )
