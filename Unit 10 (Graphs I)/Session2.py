# Problem 1: Can Rebook Flight

def can_rebook(flights, source, dest):
    # figure out in-degree/out-degree using hash-map 
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    ## source --> dest
    


    # storing position of the 1
    # 
    






flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 