"""Queue visualizer - displays queue horizontally (front to rear)."""
from typing import Any
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from .base_visualizer import BaseVisualizer


class QueueVisualizer(BaseVisualizer):
    """
    Visualizer for Queue data structure.
    Displays items horizontally with front on the left.
    """

    def __init__(self, scene: QGraphicsScene):
        """Initialize queue visualizer."""
        super().__init__(scene)
        self.start_x = 100
        self.start_y = 250

    def draw(self, queue: Any) -> None:
        """
        Draw the queue on the scene.

        Args:
            queue: Queue instance to visualize
        """
        self.clear_scene()

        if queue.is_empty():
            # Display "Empty Queue" message
            text = QGraphicsTextItem("Queue is Empty")
            text.setDefaultTextColor(self.get_text_color())
            text.setFont(QFont("Arial", 14))
            text.setPos(self.start_x + 200, self.start_y)
            self.scene.addItem(text)
            return

        items = queue.to_list()
        for i, value in enumerate(items):
            x_pos = self.start_x + (i * self.spacing)
            self._draw_node(value, x_pos, self.start_y)

        # Draw "FRONT" and "REAR" labels
        if items:
            front_label = QGraphicsTextItem("FRONT")
            front_label.setDefaultTextColor(Qt.black)
            front_label.setFont(QFont("Arial", 10, QFont.Bold))
            front_label.setPos(self.start_x, self.start_y - 40)
            self.scene.addItem(front_label)

            rear_label = QGraphicsTextItem("REAR")
            rear_label.setDefaultTextColor(Qt.black)
            rear_label.setFont(QFont("Arial", 10, QFont.Bold))
            rear_x = self.start_x + ((len(items) - 1) * self.spacing)
            rear_label.setPos(rear_x + 10, self.start_y + self.node_size + 10)
            self.scene.addItem(rear_label)

    def _draw_node(self, value: Any, x: float, y: float,
                   highlighted: bool = False, success: bool = False) -> QGraphicsRectItem:
        """
        Draw a single queue node.

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
        rect = QGraphicsRectItem(x, y, self.node_size, self.node_size)
        rect.setPen(self.get_node_pen(highlighted))
        rect.setBrush(self.get_node_brush(highlighted, success))
        self.scene.addItem(rect)

        # Draw text
        text = QGraphicsTextItem(str(value))
        text.setDefaultTextColor(self.get_text_color())
        text.setFont(QFont("Arial", 12, QFont.Bold))

        # Center text in rectangle
        text_rect = text.boundingRect()
        text_x = x + (self.node_size - text_rect.width()) / 2
        text_y = y + (self.node_size - text_rect.height()) / 2
        text.setPos(text_x, text_y)
        self.scene.addItem(text)

        return rect

    def animate_insert(self, queue: Any, value: Any, **kwargs) -> None:
        """
        Animate enqueue operation.

        Args:
            queue: Queue instance
            value: Value being enqueued
        """
        self.draw(queue)

        # Highlight the newly added rear element
        if not queue.is_empty():
            items = queue.to_list()
            rear_index = len(items) - 1
            x_pos = self.start_x + (rear_index * self.spacing)
            self._draw_node(value, x_pos, self.start_y, highlighted=True)

    def animate_delete(self, queue: Any, value: Any, **kwargs) -> None:
        """
        Animate dequeue operation.

        Args:
            queue: Queue instance
            value: Value that was dequeued
        """
        self.draw(queue)

    def animate_search(self, queue: Any, value: Any, **kwargs) -> None:
        """
        Animate search operation (highlight if found).

        Args:
            queue: Queue instance
            value: Value being searched for
        """
        self.clear_scene()

        if queue.is_empty():
            self.draw(queue)
            return

        items = queue.to_list()
        found_index = -1

        # Find the value
        for i, item in enumerate(items):
            if item == value:
                found_index = i
                break

        # Draw all nodes
        for i, item in enumerate(items):
            x_pos = self.start_x + (i * self.spacing)
            highlighted = (i == found_index)
            success = (i == found_index)
            self._draw_node(item, x_pos, self.start_y, highlighted, success)

        # Add result message
        if found_index >= 0:
            msg = QGraphicsTextItem(f"Found at position {found_index}")
            msg.setDefaultTextColor(Qt.darkGreen)
        else:
            msg = QGraphicsTextItem("Value not found")
            msg.setDefaultTextColor(Qt.darkRed)

        msg.setFont(QFont("Arial", 12, QFont.Bold))
        msg.setPos(self.start_x + 200, self.start_y - 100)
        self.scene.addItem(msg)
