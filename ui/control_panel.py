"""Control panel - operation buttons and input fields for data structures."""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                            QLineEdit, QLabel, QGroupBox, QComboBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from typing import Callable, Optional


class ControlPanel(QWidget):
    """
    Control panel for data structure operations.

    Provides buttons and inputs for insert, delete, search, etc.

    Signals:
        operation_requested: Emitted when user requests an operation
    """

    operation_requested = pyqtSignal(str, object)  # operation_name, value

    def __init__(self, ds_type: str, parent=None):
        """
        Initialize control panel.

        Args:
            ds_type: Type of data structure ('stack', 'queue', 'linked_list', 'bst')
            parent: Parent widget
        """
        super().__init__(parent)
        self.ds_type = ds_type
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize the user interface."""
        layout = QVBoxLayout()

        input_group = QGroupBox("Input")
        input_layout = QHBoxLayout()

        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("Enter value...")
        input_layout.addWidget(QLabel("Value:"))
        input_layout.addWidget(self.value_input)

        input_group.setLayout(input_layout)
        layout.addWidget(input_group)

        operations_group = QGroupBox("Operations")
        operations_layout = QVBoxLayout()

        if self.ds_type == 'stack':
            self._create_stack_buttons(operations_layout)
        elif self.ds_type == 'queue':
            self._create_queue_buttons(operations_layout)
        elif self.ds_type == 'linked_list':
            self._create_linked_list_buttons(operations_layout)
        elif self.ds_type == 'bst':
            self._create_bst_buttons(operations_layout)

        operations_group.setLayout(operations_layout)
        layout.addWidget(operations_group)

        common_group = QGroupBox("Common")
        common_layout = QVBoxLayout()

        self.clear_btn = QPushButton("Clear All")
        self.clear_btn.clicked.connect(lambda: self.operation_requested.emit('clear', None))
        common_layout.addWidget(self.clear_btn)

        common_group.setLayout(common_layout)
        layout.addWidget(common_group)

        challenge_group = QGroupBox("Challenge Mode")
        challenge_layout = QVBoxLayout()

        self.challenge_btn = QPushButton("Start Challenge")
        self.challenge_btn.clicked.connect(lambda: self.operation_requested.emit('start_challenge', None))
        challenge_layout.addWidget(self.challenge_btn)

        self.validate_btn = QPushButton("Validate Solution")
        self.validate_btn.clicked.connect(lambda: self.operation_requested.emit('validate_challenge', None))
        self.validate_btn.setEnabled(False)
        challenge_layout.addWidget(self.validate_btn)

        self.hint_btn = QPushButton("Show Hint")
        self.hint_btn.clicked.connect(lambda: self.operation_requested.emit('show_hint', None))
        self.hint_btn.setEnabled(False)
        challenge_layout.addWidget(self.hint_btn)

        challenge_group.setLayout(challenge_layout)
        layout.addWidget(challenge_group)

        layout.addStretch()
        self.setLayout(layout)

    def _create_stack_buttons(self, layout: QVBoxLayout) -> None:
        """Create buttons for stack operations."""
        push_btn = QPushButton("Push")
        push_btn.clicked.connect(lambda: self._emit_with_value('push'))
        layout.addWidget(push_btn)

        pop_btn = QPushButton("Pop")
        pop_btn.clicked.connect(lambda: self.operation_requested.emit('pop', None))
        layout.addWidget(pop_btn)

        peek_btn = QPushButton("Peek")
        peek_btn.clicked.connect(lambda: self.operation_requested.emit('peek', None))
        layout.addWidget(peek_btn)

        reverse_btn = QPushButton("Reverse Stack (Recursive)")
        reverse_btn.clicked.connect(lambda: self.operation_requested.emit('reverse', None))
        layout.addWidget(reverse_btn)

    def _create_queue_buttons(self, layout: QVBoxLayout) -> None:
        """Create buttons for queue operations."""
        enqueue_btn = QPushButton("Enqueue")
        enqueue_btn.clicked.connect(lambda: self._emit_with_value('enqueue'))
        layout.addWidget(enqueue_btn)

        dequeue_btn = QPushButton("Dequeue")
        dequeue_btn.clicked.connect(lambda: self.operation_requested.emit('dequeue', None))
        layout.addWidget(dequeue_btn)

        front_btn = QPushButton("Front")
        front_btn.clicked.connect(lambda: self.operation_requested.emit('front', None))
        layout.addWidget(front_btn)

    def _create_linked_list_buttons(self, layout: QVBoxLayout) -> None:
        """Create buttons for linked list operations."""
        insert_head_btn = QPushButton("Insert at Head")
        insert_head_btn.clicked.connect(lambda: self._emit_with_value('insert_head'))
        layout.addWidget(insert_head_btn)

        insert_tail_btn = QPushButton("Insert at Tail")
        insert_tail_btn.clicked.connect(lambda: self._emit_with_value('insert_tail'))
        layout.addWidget(insert_tail_btn)

        delete_btn = QPushButton("Delete Value")
        delete_btn.clicked.connect(lambda: self._emit_with_value('delete'))
        layout.addWidget(delete_btn)

        search_btn = QPushButton("Search")
        search_btn.clicked.connect(lambda: self._emit_with_value('search'))
        layout.addWidget(search_btn)

        find_middle_btn = QPushButton("Find Middle")
        find_middle_btn.clicked.connect(lambda: self.operation_requested.emit('find_middle', None))
        layout.addWidget(find_middle_btn)

    def _create_bst_buttons(self, layout: QVBoxLayout) -> None:
        """Create buttons for BST operations."""
        insert_btn = QPushButton("Insert")
        insert_btn.clicked.connect(lambda: self._emit_with_value('insert'))
        layout.addWidget(insert_btn)

        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(lambda: self._emit_with_value('delete'))
        layout.addWidget(delete_btn)

        search_btn = QPushButton("Search")
        search_btn.clicked.connect(lambda: self._emit_with_value('search'))
        layout.addWidget(search_btn)

        # Traversals
        inorder_btn = QPushButton("Inorder Traversal")
        inorder_btn.clicked.connect(lambda: self.operation_requested.emit('inorder', None))
        layout.addWidget(inorder_btn)

        preorder_btn = QPushButton("Preorder Traversal")
        preorder_btn.clicked.connect(lambda: self.operation_requested.emit('preorder', None))
        layout.addWidget(preorder_btn)

        postorder_btn = QPushButton("Postorder Traversal")
        postorder_btn.clicked.connect(lambda: self.operation_requested.emit('postorder', None))
        layout.addWidget(postorder_btn)

    def _emit_with_value(self, operation: str) -> None:
        """
        Emit operation signal with input value.

        Args:
            operation: Operation name
        """
        value_str = self.value_input.text().strip()
        if not value_str:
            QMessageBox.warning(self, "Input Required", "Please enter a value.")
            return

        try:
            # Try to convert to int
            value = int(value_str)
        except ValueError:
            # Keep as string if not numeric
            value = value_str

        self.operation_requested.emit(operation, value)
        self.value_input.clear()

    def enable_challenge_mode(self, enabled: bool) -> None:
        """
        Enable or disable challenge mode buttons.

        Args:
            enabled: Whether to enable challenge mode
        """
        self.validate_btn.setEnabled(enabled)
        self.hint_btn.setEnabled(enabled)
