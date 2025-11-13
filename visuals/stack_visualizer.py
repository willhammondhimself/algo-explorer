"""Stack visualizer - displays stack vertically (bottom to top)."""
from typing import Any
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem, QGraphicsItem
from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QFont
from .base_visualizer import BaseVisualizer


class StackVisualizer(BaseVisualizer):
    """
    Visualizer for Stack data structure.
    Displays items vertically with top of stack at the top.
    """

    def __init__(self, scene: QGraphicsScene):
        """Initialize stack visualizer."""
        super().__init__(scene)
        self.start_x = 350
        self.start_y = 500

    def draw(self, stack: Any) -> None:
        """
        Draw the stack on the scene.

        Args:
            stack: Stack instance to visualize
        """
        self.clear_scene()

        if stack.is_empty():
            # Display "Empty Stack" message
            text = QGraphicsTextItem("Stack is Empty")
            text.setDefaultTextColor(self.get_text_color())
            text.setFont(QFont("Arial", 14))
            text.setPos(self.start_x - 50, self.start_y - 250)
            self.scene.addItem(text)
            return

        items = stack.to_list()
        for i, value in enumerate(items):
            y_pos = self.start_y - (i * self.spacing)
            self._draw_node(value, self.start_x, y_pos)

        # Draw "TOP" label
        if items:
            top_label = QGraphicsTextItem("TOP →")
            top_label.setDefaultTextColor(Qt.black)
            top_label.setFont(QFont("Arial", 12, QFont.Bold))
            top_y = self.start_y - ((len(items) - 1) * self.spacing)
            top_label.setPos(self.start_x - 80, top_y + 10)
            self.scene.addItem(top_label)

    def _draw_node(self, value: Any, x: float, y: float,
                   highlighted: bool = False, success: bool = False) -> QGraphicsRectItem:
        """
        Draw a single stack node.

        Args:
            value: Value to display
            x: X coordinate
            y: Y coordinate
            highlighted: Whether to highlight the node
            success: Whether to show success state

        Returns:
            The created rectangle item
        """
        # Draw rectangle
        rect = QGraphicsRectItem(x, y, self.node_size * 2, self.node_size)
        rect.setPen(self.get_node_pen(highlighted))
        rect.setBrush(self.get_node_brush(highlighted, success))
        self.scene.addItem(rect)

        # Draw text
        text = QGraphicsTextItem(str(value))
        text.setDefaultTextColor(self.get_text_color())
        text.setFont(QFont("Arial", 12, QFont.Bold))

        # Center text in rectangle
        text_rect = text.boundingRect()
        text_x = x + (self.node_size * 2 - text_rect.width()) / 2
        text_y = y + (self.node_size - text_rect.height()) / 2
        text.setPos(text_x, text_y)
        self.scene.addItem(text)

        return rect

    def animate_insert(self, stack: Any, value: Any, **kwargs) -> None:
        """
        Animate push operation.

        Args:
            stack: Stack instance
            value: Value being pushed
        """
        self.draw(stack)

        # Highlight the newly added top element
        if not stack.is_empty():
            items = stack.to_list()
            top_index = len(items) - 1
            y_pos = self.start_y - (top_index * self.spacing)
            self._draw_node(value, self.start_x, y_pos, highlighted=True)

    def animate_delete(self, stack: Any, value: Any, **kwargs) -> None:
        """
        Animate pop operation.

        Args:
            stack: Stack instance
            value: Value that was popped
        """
        self.draw(stack)

    def animate_search(self, stack: Any, value: Any, **kwargs) -> None:
        """
        Animate search operation (highlight if found).

        Args:
            stack: Stack instance
            value: Value being searched for
        """
        self.clear_scene()

        if stack.is_empty():
            self.draw(stack)
            return

        items = stack.to_list()
        found_index = -1

        # Find the value
        for i, item in enumerate(items):
            if item == value:
                found_index = i
                break

        # Draw all nodes
        for i, item in enumerate(items):
            y_pos = self.start_y - (i * self.spacing)
            highlighted = (i == found_index)
            success = (i == found_index)
            self._draw_node(item, self.start_x, y_pos, highlighted, success)

        # Add result message
        if found_index >= 0:
            msg = QGraphicsTextItem(f"Found at position {found_index}")
            msg.setDefaultTextColor(Qt.darkGreen)
        else:
            msg = QGraphicsTextItem("Value not found")
            msg.setDefaultTextColor(Qt.darkRed)

        msg.setFont(QFont("Arial", 12, QFont.Bold))
        msg.setPos(self.start_x + 150, self.start_y - 250)
        self.scene.addItem(msg)
