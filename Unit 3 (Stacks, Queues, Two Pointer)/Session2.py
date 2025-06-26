# # Problem 1: Manage Performance Stage Changes
# def manage_stage_changes(changes):
#     # edge case 1: cancel/reschedule on an empty list, should re
#     # edge case 2: empty list: return an empty list
#     # cancel:pop, reschedule: pop then push
#     schedule = []
#     cancel = []
    
#     for event in changes:
#         if event.startswith("Schedule"):
#             schedule.append(event[-1])
#         elif event.startswith("Reschedule"):
#             schedule.append(cancel.pop())
#         elif event.startswith("Cancel"):
#              cancel.append(schedule.pop())

#         else:
#             return
#     return schedule

# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# # Problem 2: Queue of Performance Requests
# from collections import deque
# def process_performance_requests(requests):
#     order = deque()
#     requests.sort(reverse=True)
#     for priority, name in requests:
#         order.append(name)
#     return list(order)

# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

# # Problem 3: Collecting Points at Festival Booths
# def collect_festival_points(points):
#     stack = []
#     total_points = 0
#     for point in points:
#         stack.append(point)
#         while stack:
#             total_points += stack.pop()
#     return total_points

# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8])) 

# # Problem 4: Festival Booth Navigation
# def booth_navigation(clues):
#     stack = []
#     for clue in clues:
#         if clue == "back":
#             if stack:
#                 stack.pop()
#         else:
#             stack.append(clue)
#     return stack

# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 

# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues)) 


# # Problem 5: Merge Performance Schedules
# def merge_schedules(schedule1, schedule2):
#     merge = []
    
#     len1 = len(schedule1)
#     len2 = len(schedule2)
#     min_length = min(len1, len2)
    
#     for i in range(min_length):
#         merge.append(schedule1[i])
#         merge.append(schedule2[i])
#         len1 -= 1
#         len2 -= 1
#     if len1 > len2:
#         merge.append(schedule1[min_length])
#         merge.append(schedule1[min_length+1])
#     elif len2 > len1:
#         merge.append(schedule2[min_length])
#         merge.append(schedule2[min_length+1]) 

#     return "".join(merge)

# print(merge_schedules("abc", "pqr")) 
# print(merge_schedules("ab", "pqrs")) 
# print(merge_schedules("abcd", "pq")) 

# Problem 6: Next Greater Event
def next_greater_event(schedule1, schedule2):
  next_greater = []
  ans = []
  stack = []
  


print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4])) 