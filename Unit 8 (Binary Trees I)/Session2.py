# # Problem 1: Monstera Madness
from collections import deque

class TreeNode():
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
         
# def count_odd_splits(root):
#     if not root:
#         return 0

#     if root.val % 2 == 1:
#         return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)
#     return count_odd_splits(root.left) + count_odd_splits(root.right)


# """
#       2
#      / \
#     /   \
#    3     5
#   / \     \
#  6   7     12
# """

# # Using build_tree() function included at top of page
# values = [2, 3, 5, 6, 7, None, 12]
# monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))

# # Problem 2: Flower Finding
# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
# def find_flower(inventory, name):
#     while inventory:
#         if inventory.val == name:
#             return True
#         elif inventory.val < name:
#             inventory = inventory.right
#         else:
#             inventory = inventory.left
#     return False


# """
#           Rose
#          /    \
#       Lilac  Tulip
#       /  \       \
#    Daisy Lily   Violet
# """

# # using build_tree() function at top of page
# values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
# garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower"))

# Problem 3: Flower Finding II
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

"""
         Daisy
        /    \
      Lily   Tulip
     /  \       \
  Rose  Violet  Lilac
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))  
print(non_bst_find_flower(garden, "Sunflower")) 

# Problem 4: Adding a New Plant to the Collection
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_plant(collection, name):
    current = collection
    while current:
        if current.val == current:
            current = current.right
        elif current.val < name:
            if not current.right:
                current.right = TreeNode(name)
                return collection
            else:
                current = current.right
        else:
            if not current.left:
                current.left = TreeNode(name)
                return collection
            else:
                current = current.left
    return collection

"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))

# Problem 5: Sorting Plants by Rarity
class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key      # Plant price
        self.val = value      # Plant name
        self.left = left
        self.right = right


def sort_plants(collection):
    pass

"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))