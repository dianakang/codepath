# Problem 1 - Problem 1
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) > 20:
            print("Invalid catchphrase.")
        else:
            self.catchphrase = new_catchphrase
            print("catchphrase updated")
            return new_catchphrase
    
    def add_item(self, item_name):
        new_furniture = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        
        if item_name in new_furniture:
            self.furniture.append(item_name)

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def print_inventory(self):
        # Implement the method here
        inventory = {}
        
        if not self.furniture:
            print("No furniture in inventory.")
        else:
            for stuff in self.furniture:
                inventory[stuff] = inventory.get(stuff, 0) + 1
            print(inventory)
    
    def of_personality_type(self, personality_type):
        personality_types = ["jock", "snooty", "normal", "lazy", "peppy", "smug", "cranky", "big sister", "sisterly"]
        
        if personality_type in personality_types:
            return f"{self.name} is a {personality_type} villager."
        else:
            return f"{self.name} does not have a valid personality type."


def of_personality_type(townies, personality_type):
    name = []
    for villager in townies:
        if villager.personality == personality_type:
            name.append(villager.name)
    return name
    
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))


