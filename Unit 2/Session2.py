# # Session 2: Dictionaries & Sets
# ## Standard Problem Set Version 1
# ### Problem 1: Most Endangered Species
# def most_endangered(species_list):
#     index = 0
#     lowest_population = float('inf')

#     for i, entry in enumerate(species_list):
#         if entry["population"] < lowest_population:
#             index = i
#             lowest_population = entry["population"]

#     return species_list[index]["name"]

# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list))


# ### Problem 2: Identifying Endangered Species
# def count_endangered_species(endangered_species, observed_species):
#     total = 0
#     for animal in observed_species:
#         if animal in endangered_species:
#             total += 1
#     return total

# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2)) 


# ### Problem 3: Navigating the Research Station (sentinel value)
# def navigate_research_station(station_layout, observations):
#     observations = station_layout[0] + observations
#     # print(observations)
#     total = 0

#     lookup = {}

#     for i, val in enumerate(station_layout):
#         lookup[val] = i

#     for i in range(len(observations) - 1):
#         total += abs(lookup[observations[i]] - lookup[observations[i + 1]])

#     return total

# station_layout1 = "pqrstuvwxyzabcdefghijklmno"
# observations1 = "wildlife"

# station_layout2 = "abcdefghijklmnopqrstuvwxyz"
# observations2 = "cba"

# print(navigate_research_station(station_layout1, observations1))  
# print(navigate_research_station(station_layout2, observations2))


### Problem 4: Prioritizing Endangered Species Observations
def prioritize_observations(observed_species, priority_species):
    result = []
    not_in_priority = []

    for item in priority_species:
        for item2 in observed_species:
            if item == item2:
                result.append(item)
    
    for item in observed_species:
        if item not in priority_species:
            not_in_priority.append(item)
    not_in_priority.sort()

    result.extend(not_in_priority)
    return result

  

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 