"""Linked List visualizer - displays nodes horizontally with arrows."""
from typing import Any
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem
from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QFont, QPen
from .base_visualizer import BaseVisualizer


class LinkedListVisualizer(BaseVisualizer):
    """
    Visualizer for Singly Linked List data structure.
    Displays nodes horizontally with arrows showing connections.
    """

    def __init__(self, scene: QGraphicsScene):
        """Initialize linked list visualizer."""
        super().__init__(scene)
        self.start_x = 100
        self.start_y = 250
        self.spacing = 120

    def draw(self, linked_list: Any) -> None:
        """
        Draw the linked list on the scene.

        Args:
            linked_list: LinkedList instance to visualize
        """
        self.clear_scene()

        if linked_list.is_empty():
            # Display "Empty List" message
            text = QGraphicsTextItem("Linked List is Empty")
            text.setDefaultTextColor(self.get_text_color())
            text.setFont(QFont("Arial", 14))
            text.setPos(self.start_x + 200, self.start_y)
            self.scene.addItem(text)
            return

        items = linked_list.to_list()
        for i, value in enumerate(items):
            x_pos = self.start_x + (i * self.spacing)
            self._draw_node(value, x_pos, self.start_y)

            # Draw arrow to next node (except for last node)
            if i < len(items) - 1:
                self._draw_arrow(x_pos + self.node_size, self.start_y + self.node_size / 2,
                               x_pos + self.spacing, self.start_y + self.node_size / 2)

        # Draw "HEAD" label
        if items:
            head_label = QGraphicsTextItem("HEAD")
            head_label.setDefaultTextColor(Qt.black)
            head_label.setFont(QFont("Arial", 10, QFont.Bold))
            head_label.setPos(self.start_x, self.start_y - 40)
            self.scene.addItem(head_label)

        # Draw "NULL" at the end
        if items:
            null_label = QGraphicsTextItem("NULL")
            null_label.setDefaultTextColor(Qt.darkRed)
            null_label.setFont(QFont("Arial", 10, QFont.Bold))
            null_x = self.start_x + (len(items) * self.spacing)
            null_label.setPos(null_x, self.start_y + 10)
            self.scene.addItem(null_label)

    def _draw_node(self, value: Any, x: float, y: float,
                   highlighted: bool = False, success: bool = False) -> QGraphicsEllipseItem:
        """
        Draw a single linked list node.

        Args:
            value: Value to display
            x: X coordinate
            y: Y coordinate
            highlighted: Whether to highlight the node
            success: Whether to show success state

        Returns:
            The created ellipse item
        """
        # Draw circle
        circle = QGraphicsEllipseItem(x, y, self.node_size, self.node_size)
        circle.setPen(self.get_node_pen(highlighted))
        circle.setBrush(self.get_node_brush(highlighted, success))
        self.scene.addItem(circle)

        # Draw text
        text = QGraphicsTextItem(str(value))
        text.setDefaultTextColor(self.get_text_color())
        text.setFont(QFont("Arial", 12, QFont.Bold))

        # Center text in circle
        text_rect = text.boundingRect()
        text_x = x + (self.node_size - text_rect.width()) / 2
        text_y = y + (self.node_size - text_rect.height()) / 2
        text.setPos(text_x, text_y)
        self.scene.addItem(text)

        return circle

    def _draw_arrow(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """
        Draw an arrow between two points.

        Args:
            x1: Start X coordinate
            y1: Start Y coordinate
            x2: End X coordinate
            y2: End Y coordinate
        """
        line = QGraphicsLineItem(QLineF(x1, y1, x2 - 10, y2))
        line.setPen(self.get_arrow_pen())
        self.scene.addItem(line)

        # Draw arrowhead
        arrow_size = 10
        arrow_line1 = QGraphicsLineItem(QLineF(x2 - 10, y2, x2 - 10 - arrow_size, y2 - arrow_size / 2))
        arrow_line2 = QGraphicsLineItem(QLineF(x2 - 10, y2, x2 - 10 - arrow_size, y2 + arrow_size / 2))
        arrow_line1.setPen(self.get_arrow_pen())
        arrow_line2.setPen(self.get_arrow_pen())
        self.scene.addItem(arrow_line1)
        self.scene.addItem(arrow_line2)

    def animate_insert(self, linked_list: Any, value: Any, **kwargs) -> None:
        """
        Animate insertion operation.

        Args:
            linked_list: LinkedList instance
            value: Value being inserted
        """
        self.draw(linked_list)

        # Highlight the newly inserted node
        position = kwargs.get('position', -1)
        if position >= 0:
            items = linked_list.to_list()
            if position < len(items):
                x_pos = self.start_x + (position * self.spacing)
                self._draw_node(items[position], x_pos, self.start_y, highlighted=True)

    def animate_delete(self, linked_list: Any, value: Any, **kwargs) -> None:
        """
        Animate deletion operation.

        Args:
            linked_list: LinkedList instance
            value: Value that was deleted
        """
        self.draw(linked_list)

    def animate_search(self, linked_list: Any, value: Any, **kwargs) -> None:
        """
        Animate search operation (highlight if found).

        Args:
            linked_list: LinkedList instance
            value: Value being searched for
        """
        self.clear_scene()

        if linked_list.is_empty():
            self.draw(linked_list)
            return

        items = linked_list.to_list()
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

            # Draw arrows
            if i < len(items) - 1:
                self._draw_arrow(x_pos + self.node_size, self.start_y + self.node_size / 2,
                               x_pos + self.spacing, self.start_y + self.node_size / 2)

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
