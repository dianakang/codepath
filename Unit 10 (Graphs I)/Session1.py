# # Problem 1: Graphing Flights
# """
# JFK ----- LAX
# |
# |
# DFW ----- ATL
# """
# # No starter code is provided for this problem
# # Add your code here
# flights = { 
#     "JFK": ["LAX", "DFW"],
#     "LAX": ["JFK"],
#     "DFW": ["JFK", "ATL"],
#     "ATL": ["DFW"]
# }

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])

# # Problem 2: There and Back
# def bidirectional_flights(flights):
#     for i in range(len(flights)):
#         for j in flights[i]:
#             if i not in flights[j]:
#                 return False
#     return True

# flights1 = [[1, 2], [0], [0, 3], [2]]
# flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))

# Problem 3: Finding Direct Flights
def get_direct_flights(flights, source):
    pass


flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))