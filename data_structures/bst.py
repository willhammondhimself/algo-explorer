"""Binary Search Tree data structure implementation."""
import copy


class TreeNode:
    """
    Node for binary search tree.    """

    def __init__(self, data):
        """
        Initialize a tree node with data.        """
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        """String representation of the node."""
        return f"TreeNode({self.data})"

    def __repr__(self):
        """Detailed representation of the node."""
        return f"TreeNode(data={self.data})"


class BinarySearchTree:
    """
    Binary Search Tree data structure.    """

    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root = None
        self.size_count: int = 0

    def insert(self, data):
        """
        Insert a value into the tree.        """
        if self.root is None:
            self.root = TreeNode(data)
            self.size_count += 1
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """
        Recursively insert a value into the tree.        """
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
                self.size_count += 1
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
                self.size_count += 1
            else:
                self._insert_recursive(node.right, data)
        # If data == node.data, ignore (no duplicates)

    def search(self, data):
        """
        Search for a value in the tree.
        """
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        """
        Recursively search for a value.
        """
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def delete(self, data):
        """
        Delete a value from the tree.
        """
        # TODO: could optimize this with iterative approach instead of recursive
        # but recursion is clearer for understanding the algorithm
        if not self.search(data):
            return False
        self.root = self._delete_recursive(self.root, data)
        return True

    def _delete_recursive(self, node, data):
        """
        Recursively delete a value from the tree.            Updated node after deletion
        """
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node with only one child or no child
            if node.left is None:
                self.size_count -= 1
                return node.right
            elif node.right is None:
                self.size_count -= 1
                return node.left

            # Node with two children: get inorder successor
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data
            node.right = self._delete_recursive(node.right, min_larger_node.data)

        return node

    def _find_min(self, node):
        """
        Find the minimum value node in a subtree.            Node with minimum value
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        """
        Perform inorder traversal (left, root, right).        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper for inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        """
        Perform preorder traversal (root, left, right).        """
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        """Helper for preorder traversal."""
        if node is not None:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """
        Perform postorder traversal (left, right, root).        """
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        """Helper for postorder traversal."""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)

    def is_empty(self):
        """Check if the tree is empty."""
        return self.root is None

    def size(self):
        """Return the number of nodes in the tree."""
        return self.size_count

    def clear(self):
        """Remove all nodes from the tree."""
        self.root = None
        self.size_count = 0

    def get_state(self):
        """
        Get the current state for serialization.        """
        return {
            "items": self.preorder_traversal(),
            "size": self.size_count
        }

    def set_state(self, state):
        """
        Restore the tree from a saved state.        """
        self.clear()
        for item in state["items"]:
            self.insert(item)

    @staticmethod
    def build_balanced_from_sorted(sorted_array) -> 'BinarySearchTree':
        """
        Build a balanced BST from a sorted array.
        Used for challenge mode.            Balanced binary search tree
        """
        bst = BinarySearchTree()
        bst.root = BinarySearchTree._build_balanced_recursive(sorted_array, 0, len(sorted_array) - 1)
        bst.size_count = len(sorted_array)
        return bst

    @staticmethod
    def _build_balanced_recursive(arr, start, end):
        """
        Recursively build balanced tree from sorted array.            Root node of the balanced subtree
        """
        if start > end:
            return None

        mid = (start + end) // 2
        node = TreeNode(arr[mid])
        node.left = BinarySearchTree._build_balanced_recursive(arr, start, mid - 1)
        node.right = BinarySearchTree._build_balanced_recursive(arr, mid + 1, end)
        return node

    def __str__(self):
        """String representation of the tree."""
        return f"BST(inorder={self.inorder_traversal()})"

    def __repr__(self):
        """Detailed representation of the tree."""
        return f"BinarySearchTree(size={self.size_count}, inorder={self.inorder_traversal()})"
