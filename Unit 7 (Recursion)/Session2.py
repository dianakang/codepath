# # Problem 2: Booking the Perfect Cruise Cabin
# def find_cabin_index(cabins, preferred_deck):
#     left = 0
#     right = len(cabins) - 1

#     def helper(left, right):
#         mid = (left+right) // 2
#         if left >= right:
#             return mid + 1
#         elif cabins[mid] == preferred_deck:
#             return mid
#         elif cabins[mid] > preferred_deck:
#             return helper(left, mid - 1)
#         else:
#             return helper(mid+1, right)

#     return helper(left, right)

# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))

# # Problem 3: Count Checked In Passengers
# def count_checked_in_passengers(rooms):
#     left = 0
#     right = len(rooms) - 1

#     if rooms[left] == 1:
#         return len(rooms)

#     while left <= right:
#         mid = (left+right) // 2
#         if rooms[mid] == 1:
#             right = mid - 1
#             if rooms[mid-1] == 0:
#                 return len(rooms[mid:])
#         else:
#             left = mid + 1
#     return 0

# rooms1 = [0, 0, 0, 1, 1, 1, 1]
# rooms2 = [0, 0, 0, 0, 0, 1]
# rooms3 = [0, 0, 0, 0, 0, 0]

# print(count_checked_in_passengers(rooms1)) 
# print(count_checked_in_passengers(rooms2))
# print(count_checked_in_passengers(rooms3))

# Problem 4: Determining Profitability of Excursions
def is_profitable(excursion_counts):
    pass

print(is_profitable([3, 5]))
print(is_profitable([0, 0]))