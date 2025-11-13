"""Base visualizer class for all data structure visualizations."""
from abc import ABC, abstractmethod
from typing import Any, Optional
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsItem
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QObject, pyqtProperty, QPointF
from PyQt5.QtGui import QColor, QPen, QBrush


# Color scheme: Academic blue/white/black
COLORS = {
    "primary": QColor(41, 128, 185),      # Blue
    "secondary": QColor(52, 152, 219),    # Light blue
    "background": QColor(255, 255, 255),  # White
    "text": QColor(0, 0, 0),              # Black
    "highlight": QColor(231, 76, 60),     # Red for highlighting
    "success": QColor(46, 204, 113),      # Green
    "border": QColor(44, 62, 80)          # Dark gray
}


class AnimatedItem(QObject):
    """
    Wrapper for QGraphicsItem to enable property animations.

    Attributes:
        item: The QGraphicsItem being animated
        _pos: Current position of the item
    """

    def __init__(self, item: QGraphicsItem):
        """Initialize animated item wrapper."""
        super().__init__()
        self.item = item
        self._pos = item.pos()

    def get_pos(self) -> QPointF:
        """Get current position."""
        return self._pos

    def set_pos(self, pos: QPointF) -> None:
        """Set position and update item."""
        self._pos = pos
        self.item.setPos(pos)

    pos = pyqtProperty(QPointF, get_pos, set_pos)


class BaseVisualizer(ABC):
    """
    Abstract base class for all data structure visualizers.

    Provides common animation infrastructure and rendering utilities.
    """

    def __init__(self, scene: QGraphicsScene):
        """
        Initialize the base visualizer.

        Args:
            scene: QGraphicsScene for rendering
        """
        self.scene = scene
        self.animations = []
        self.node_size = 50
        self.spacing = 80

    @abstractmethod
    def draw(self, data_structure: Any) -> None:
        """
        Draw the data structure on the scene.

        Args:
            data_structure: The data structure to visualize
        """
        pass

    @abstractmethod
    def animate_insert(self, data_structure: Any, value: Any, **kwargs) -> None:
        """
        Animate insertion operation.

        Args:
            data_structure: The data structure
            value: Value being inserted
            **kwargs: Additional animation parameters
        """
        pass

    @abstractmethod
    def animate_delete(self, data_structure: Any, value: Any, **kwargs) -> None:
        """
        Animate deletion operation.

        Args:
            data_structure: The data structure
            value: Value being deleted
            **kwargs: Additional animation parameters
        """
        pass

    @abstractmethod
    def animate_search(self, data_structure: Any, value: Any, **kwargs) -> None:
        """
        Animate search operation.

        Args:
            data_structure: The data structure
            value: Value being searched for
            **kwargs: Additional animation parameters
        """
        pass

    def clear_scene(self) -> None:
        """Clear all items from the scene."""
        self.scene.clear()
        self.animations.clear()

    def create_animation(self, item: QGraphicsItem, start_pos: QPointF,
                        end_pos: QPointF, duration: int = 500) -> QPropertyAnimation:
        """
        Create a position animation for a graphics item.

        Args:
            item: Graphics item to animate
            start_pos: Starting position
            end_pos: Ending position
            duration: Animation duration in milliseconds

        Returns:
            Configured QPropertyAnimation
        """
        animated_item = AnimatedItem(item)
        animation = QPropertyAnimation(animated_item, b"pos")
        animation.setDuration(duration)
        animation.setStartValue(start_pos)
        animation.setEndValue(end_pos)
        animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.animations.append((animation, animated_item))
        return animation

    def get_node_pen(self, highlighted: bool = False) -> QPen:
        """
        Get pen for drawing node borders.

        Args:
            highlighted: Whether the node is highlighted

        Returns:
            QPen object with appropriate color
        """
        color = COLORS["highlight"] if highlighted else COLORS["border"]
        pen = QPen(color, 2)
        return pen

    def get_node_brush(self, highlighted: bool = False, success: bool = False) -> QBrush:
        """
        Get brush for filling nodes.

        Args:
            highlighted: Whether the node is highlighted
            success: Whether to show success state

        Returns:
            QBrush object with appropriate color
        """
        if success:
            color = COLORS["success"]
        elif highlighted:
            color = COLORS["secondary"]
        else:
            color = COLORS["primary"]
        return QBrush(color)

    def get_text_color(self) -> QColor:
        """Get color for text."""
        return COLORS["background"]  # White text on colored nodes

    def get_arrow_pen(self) -> QPen:
        """Get pen for drawing arrows/connections."""
        return QPen(COLORS["border"], 2)
