# # Problem 1: Grafting Apples
# from collections import deque 
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# # Tree Node class
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def print_tree(root):
#     if not root:
#         return "Empty"
#     result = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#     while result and result[-1] is None:
#         result.pop()
#     print(result)

# # Create the leaf nodes
# Fuji = TreeNode("Fuji")
# Opal = TreeNode("Opal")
# Crab = TreeNode("Crab")
# Gala = TreeNode("Gala")
# # Create the Parent node
# GrannySmith = TreeNode("Granny Smith", Crab, Gala)
# McIntosh = TreeNode("McIntosh", Fuji, Opal)
# # Create root node
# root = TreeNode("Trunk", McIntosh, GrannySmith)

# # Using print_tree() included at the top of this page
# print_tree(root)

# # Problem 2: Calculating Yield
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def calculate_yield(root):
#     if root.val == "+":
#         return root.left.val + root.right.val
#     if root.val == "-":
#         return root.left.val - root.right.val
#     if root.val == "*":
#         return root.left.val * root.right.val
#     if root.val == "/":
#         return root.left.val / root.right.val

# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))

# Problem 3: Ivy Cutting
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
  pass

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))