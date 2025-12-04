# Q. given string day, return index of day. if invalid day, return -1
# i/p: Sunday, o/p: 0
# i/p: Monday, o/p: 1
dic = {"Sunday": 0,
       "Monday": 1,
       "Tuesday": 2,
       "Wednesday": 3,
       "Thursday": 4,
       "Friday": 5,
       "Saturday": 6}

def day_to_number(day: str) -> int:
    solution = -1
    for day in dic.keys():
        # edge case
        if day is not dic.keys:
            # return dic.get(day,-1)
            solution = dic.get(day,-1)
        else:
            # return dic[day]
            solution = dic[day]
    return solution

# test case
if __name__ == "__main__":
    print(day_to_number("Wednesday"))
    print(day_to_number("Saturday"))    
    print(day_to_number("tejas"))    