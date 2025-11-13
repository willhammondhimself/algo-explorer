"""Animation canvas - custom QGraphicsView for rendering visualizations."""
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter


class AnimationCanvas(QGraphicsView):
    """
    Custom QGraphicsView for displaying data structure visualizations.

    Provides smooth rendering and interaction capabilities.
    """

    def __init__(self, parent=None):
        """
        Initialize the animation canvas.

        Args:
            parent: Parent widget
        """
        super().__init__(parent)

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.scene.setSceneRect(0, 0, 800, 600)

        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setRenderHint(QPainter.TextAntialiasing)

        self.setStyleSheet("background-color: white;")
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setMinimumSize(800, 600)

    def clear(self) -> None:
        """Clear the canvas."""
        self.scene.clear()

    def get_scene(self) -> QGraphicsScene:
        """
        Get the graphics scene.

        Returns:
            QGraphicsScene instance
        """
        return self.scene

    def wheelEvent(self, event) -> None:
        """
        Handle mouse wheel events for zooming.

        Args:
            event: Wheel event
        """
        # Zoom in/out with mouse wheel
        zoom_factor = 1.15
        if event.angleDelta().y() > 0:
            # Zoom in
            self.scale(zoom_factor, zoom_factor)
        else:
            # Zoom out
            self.scale(1 / zoom_factor, 1 / zoom_factor)
