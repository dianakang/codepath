# # Problem 1: Counting Iron Man's Suits
# def count_suits_iterative(suits):
#     count = 0
    
#     for suit in suits:
#         count+=1
#     return count

# def count_suits_recursive(suits):
#     if suits == []:
#         return 0
    
#     return count_suits_recursive([:1]) + 1

# # Problem 2: Collecting Infinity Stones
# def sum_stones(stones):
#     if not stones:
#         return 0
    
#     return stones[0] + sum_stones(stones[1:])

# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

# # Problem 3: Counting Unique Suits
# def count_suits_iterative(suits):
#     total = set(suits)
#     return len(total)

# def count_suits_recursive(suits):
#     if suits == []:
#         return 0
    
#     if suits[0] in suits[1:]:
#         return count_suits_recursive(suits[1:])
#     else:
#         return count_suits_recursive(suits[1:]) + 1

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

# # Problem 4: Calculating Groot's Growth
# def fibonacci_growth(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_growth(n-1) + fibonacci_growth(n-2)

# print(fibonacci_growth(5))
# print(fibonacci_growth(8))

# # Problem 5: Calculating the Power of the Fantastic Four
# def power_of_four(n):
#     if n == 0:
#         return 1
    
#     if n > 0:
#         return 4 * power_of_four(n-1)

#     return 1 / (4 * power_of_four(-n-1))

# print(power_of_four(2))
# print(power_of_four(-2))

# # Problem 6: Strongest Avenger
# def strongest_avenger(strengths):
#     if len(strengths)==1:
#         return strengths[0]
    
#     max_of_rest = strongest_avenger(strengths[1:])
#     if strengths[0] <= max_of_rest:
#         return max_of_rest
#     else:
#         return strengths[0]
        
# print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
# print(strongest_avenger([50, 75, 85, 60, 90]))

# Problem 7: Counting Vibranium Deposits
def count_deposits(resources):
    if len(resources) == 0:
        return 0
    elif resources[0] == "V":
        return count_deposits(resources[1:])+1
    else:
        return count_deposits(resources[1:])

print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))