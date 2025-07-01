# class Solution:
#     def isValid(self, s: str) -> bool:
#         ss = []
#         for i in s:
#             if i == '[' or i == '{' or i == '(':
#                 ss.append(i)
#             elif i == ']' :
#                 if not ss or not ss.pop() == '[':
#                     return False
#             elif i == '}' :
#                 if not ss or not ss.pop() == '{':
#                     return False
#             elif i == ')' :
#                 if not ss or not ss.pop() == '(':
#                     return False
#         return not ss


def mystery_function(nums):
    left = len(nums) - 1
    right = len(nums) - 1
    
    while right >= 0:
        if nums[right] != 0:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left -= 1
        right -= 1
    return nums

nums = [0, 0, 1, 2, 0, 3]
print(mystery_function(nums))  # Output: [1, 2, 3, 0, 0, 0]