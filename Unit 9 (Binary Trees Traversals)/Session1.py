from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

# def merge_orders(order1, order2):
#     if order1 is None:
#         return order2
#     elif order2 is None:
#         return order1

#     # 1. create new tree nodege_
#     new_tree = TreeNode(order1.val + order2.val)
#     new_tree.right = merge_orders(order1.right, order2.right)
#     new_tree.left = merge_orders(order1.left, order2.left)

#     return new_tree

# """
#      1             2         
#     /  \         /   \       
#    3    2       1     3   
#  /               \      \   
# 5                 4      7   
# """
# # Using build_tree() function included at top of page
# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)

# # Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))

# # Problem 2: Croquembouche
# class Puff():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def print_design(design):
#     # Create a base case to check for edge cases
#     if not design:
#         print([])
#         return None
    
#     # Create an empty array to initialize the flover list and start with the root
#     flavor = []
#     queue = deque()

#     queue.append(design)

#     while queue:
#         first_item = queue.popleft()
#         flavor.append(first_item.val)

#         # Add to left and right children if the value exist
#         if first_item.left:
#             queue.append(first_item.left)
#         if first_item.right:
#             queue.append(first_item.right)

#     print(flavor) 

# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))
# print_design(croquembouche)


# Problem 3: Maximum Tiers in Cake
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if cake is None:
        return 0
    
    left_dep = max_tiers(cake.left)
    right_dep = max_tiers(cake.right)
    return max(left_dep, right_dep) + 1

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))