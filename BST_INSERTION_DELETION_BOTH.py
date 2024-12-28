# Define a Node class to represent each node in the Binary Search Tree (BST)
class Node:
    def __init__(self, value):
        # Initialize the node with a value, and left and right child nodes set to None
        self.value = value
        self.left = None
        self.right = None

# Function to insert a new value into the BST
def insert_node(root, value):
    # If the tree is empty, create a new node with the given value
    if root is None:
        return Node(value)
    else:
        # If the value is less than the current node's value, insert it into the left subtree
        if value < root.value:
            root.left = insert_node(root.left, value)
        # If the value is greater than the current node's value, insert it into the right subtree
        else:
            root.right = insert_node(root.right, value)
    return root

# Function to find the node with the minimum value in a subtree
def find_min_node(node):
    # Traverse the subtree to find the node with the minimum value
    current = node
    while current.left is not None:
        current = current.left
    return current

# Function to delete a node from the BST
def delete_node(root, value):
    # If the tree is empty, return None
    if root is None:
        return root
    # If the value to be deleted is less than the current node's value, delete it from the left subtree
    if value < root.value:
        root.left = delete_node(root.left, value)
    # If the value to be deleted is greater than the current node's value, delete it from the right subtree
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        # If the node to be deleted has no children, simply remove it
        if root.left is None:
            temp = root.right
            root = None
            return temp
        # If the node to be deleted has one child, replace it with its child
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # If the node to be deleted has two children, find the node with the minimum value in the right subtree,
        # replace the node to be deleted with that node, and then delete the minimum node from the right subtree
        else:
            temp = find_min_node(root.right)
            root.value = temp.value
            root.right = delete_node(root.right, temp.value)
    return root

# Helper function to print the inorder traversal of the tree
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Example usage:
root = None
root = insert_node(root, 50)
root = insert_node(root, 30)
root = insert_node(root, 20)
root = insert_node(root, 40)
root = insert_node(root, 70)
root = insert_node(root, 60)
root = insert_node(root, 80)

print("Inorder traversal of the given tree:")
inorder_traversal(root)

print("Delete 20")
root = delete_node(root, 20)
print("Inorder traversal of the modified tree:")
inorder_traversal(root)

print("Delete 30")
root = delete_node(root, 30)
print("Inorder traversal of the modified tree:")
inorder_traversal(root)

print("Delete 50")
root = delete_node(root, 50)
print("Inorder traversal of the modified tree:")
inorder_traversal(root)