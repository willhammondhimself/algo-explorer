"""BST visualizer - displays tree structure with proper layout."""
from typing import Any, Optional, Dict
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem
from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QFont
from .base_visualizer import BaseVisualizer


class BSTVisualizer(BaseVisualizer):
    """
    Visualizer for Binary Search Tree data structure.
    Displays tree with proper hierarchical layout.
    """

    def __init__(self, scene: QGraphicsScene):
        """Initialize BST visualizer."""
        super().__init__(scene)
        self.start_x = 400
        self.start_y = 50
        self.level_height = 80
        self.horizontal_spacing = 60

    def draw(self, bst: Any) -> None:
        """
        Draw the BST on the scene.

        Args:
            bst: BinarySearchTree instance to visualize
        """
        self.clear_scene()

        if bst.is_empty():
            # Display "Empty Tree" message
            text = QGraphicsTextItem("Binary Search Tree is Empty")
            text.setDefaultTextColor(self.get_text_color())
            text.setFont(QFont("Arial", 14))
            text.setPos(self.start_x - 100, self.start_y + 200)
            self.scene.addItem(text)
            return

        # Calculate positions for all nodes
        positions = self._calculate_positions(bst.root)

        # Draw edges first (so they appear behind nodes)
        self._draw_edges(bst.root, positions)

        # Draw nodes
        self._draw_nodes(bst.root, positions)

    def _calculate_positions(self, root: Optional[Any]) -> Dict:
        """
        Calculate positions for all nodes using in-order traversal.

        Args:
            root: Root TreeNode

        Returns:
            Dictionary mapping node to (x, y) position
        """
        positions = {}
        self._inorder_position = 0

        def calculate_inorder_index(node: Optional[Any], depth: int = 0) -> None:
            if node is None:
                return

            calculate_inorder_index(node.left, depth + 1)

            x = self.start_x + (self._inorder_position * self.horizontal_spacing) - \
                (self._count_nodes(root) * self.horizontal_spacing / 2)
            y = self.start_y + (depth * self.level_height)
            positions[id(node)] = (x, y, depth)
            self._inorder_position += 1

            calculate_inorder_index(node.right, depth + 1)

        calculate_inorder_index(root)
        return positions

    def _count_nodes(self, node: Optional[Any]) -> int:
        """
        Count total nodes in tree.

        Args:
            node: TreeNode

        Returns:
            Number of nodes
        """
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def _draw_edges(self, node: Optional[Any], positions: Dict) -> None:
        """
        Recursively draw edges between nodes.

        Args:
            node: Current TreeNode
            positions: Position dictionary
        """
        if node is None:
            return

        node_id = id(node)
        if node_id not in positions:
            return

        x, y, depth = positions[node_id]
        center_x = x + self.node_size / 2
        center_y = y + self.node_size / 2

        # Draw edge to left child
        if node.left is not None:
            left_id = id(node.left)
            if left_id in positions:
                left_x, left_y, _ = positions[left_id]
                left_center_x = left_x + self.node_size / 2
                left_center_y = left_y + self.node_size / 2
                line = QGraphicsLineItem(QLineF(center_x, center_y, left_center_x, left_center_y))
                line.setPen(self.get_arrow_pen())
                self.scene.addItem(line)
                self._draw_edges(node.left, positions)

        # Draw edge to right child
        if node.right is not None:
            right_id = id(node.right)
            if right_id in positions:
                right_x, right_y, _ = positions[right_id]
                right_center_x = right_x + self.node_size / 2
                right_center_y = right_y + self.node_size / 2
                line = QGraphicsLineItem(QLineF(center_x, center_y, right_center_x, right_center_y))
                line.setPen(self.get_arrow_pen())
                self.scene.addItem(line)
                self._draw_edges(node.right, positions)

    def _draw_nodes(self, node: Optional[Any], positions: Dict,
                   highlight_value: Any = None, success_value: Any = None) -> None:
        """
        Recursively draw all nodes.

        Args:
            node: Current TreeNode
            positions: Position dictionary
            highlight_value: Value to highlight
            success_value: Value to show as success
        """
        if node is None:
            return

        node_id = id(node)
        if node_id not in positions:
            return

        x, y, depth = positions[node_id]

        highlighted = (node.data == highlight_value)
        success = (node.data == success_value)

        # Draw circle
        circle = QGraphicsEllipseItem(x, y, self.node_size, self.node_size)
        circle.setPen(self.get_node_pen(highlighted))
        circle.setBrush(self.get_node_brush(highlighted, success))
        self.scene.addItem(circle)

        # Draw text
        text = QGraphicsTextItem(str(node.data))
        text.setDefaultTextColor(self.get_text_color())
        text.setFont(QFont("Arial", 12, QFont.Bold))

        # Center text in circle
        text_rect = text.boundingRect()
        text_x = x + (self.node_size - text_rect.width()) / 2
        text_y = y + (self.node_size - text_rect.height()) / 2
        text.setPos(text_x, text_y)
        self.scene.addItem(text)

        # Recursively draw children
        self._draw_nodes(node.left, positions, highlight_value, success_value)
        self._draw_nodes(node.right, positions, highlight_value, success_value)

    def animate_insert(self, bst: Any, value: Any, **kwargs) -> None:
        """
        Animate insertion operation.

        Args:
            bst: BinarySearchTree instance
            value: Value being inserted
        """
        self.clear_scene()

        if bst.is_empty():
            self.draw(bst)
            return

        # Calculate positions
        positions = self._calculate_positions(bst.root)

        # Draw edges
        self._draw_edges(bst.root, positions)

        # Draw nodes with highlighting
        self._draw_nodes(bst.root, positions, highlight_value=value)

    def animate_delete(self, bst: Any, value: Any, **kwargs) -> None:
        """
        Animate deletion operation.

        Args:
            bst: BinarySearchTree instance
            value: Value that was deleted
        """
        self.draw(bst)

    def animate_search(self, bst: Any, value: Any, **kwargs) -> None:
        """
        Animate search operation (highlight if found).

        Args:
            bst: BinarySearchTree instance
            value: Value being searched for
        """
        self.clear_scene()

        if bst.is_empty():
            self.draw(bst)
            return

        # Calculate positions
        positions = self._calculate_positions(bst.root)

        # Draw edges
        self._draw_edges(bst.root, positions)

        # Check if value exists
        found = bst.search(value)

        # Draw nodes with highlighting
        if found:
            self._draw_nodes(bst.root, positions, success_value=value)
            msg = QGraphicsTextItem(f"Value {value} found in tree")
            msg.setDefaultTextColor(Qt.darkGreen)
        else:
            self._draw_nodes(bst.root, positions)
            msg = QGraphicsTextItem(f"Value {value} not found")
            msg.setDefaultTextColor(Qt.darkRed)

        msg.setFont(QFont("Arial", 12, QFont.Bold))
        msg.setPos(self.start_x - 100, self.start_y + 400)
        self.scene.addItem(msg)

    def draw_traversal(self, bst: Any, traversal_type: str) -> None:
        """
        Visualize tree traversal by showing the order.

        Args:
            bst: BinarySearchTree instance
            traversal_type: Type of traversal ('inorder', 'preorder', 'postorder')
        """
        self.draw(bst)

        if bst.is_empty():
            return

        # Get traversal result
        if traversal_type == 'inorder':
            result = bst.inorder_traversal()
        elif traversal_type == 'preorder':
            result = bst.preorder_traversal()
        elif traversal_type == 'postorder':
            result = bst.postorder_traversal()
        else:
            return

        # Display traversal result
        result_text = f"{traversal_type.capitalize()}: {' → '.join(str(x) for x in result)}"
        msg = QGraphicsTextItem(result_text)
        msg.setDefaultTextColor(Qt.black)
        msg.setFont(QFont("Arial", 11, QFont.Bold))
        msg.setPos(50, self.start_y + 400)
        self.scene.addItem(msg)
