# # Problem 1: Post Format Validator
# def is_valid_post_format(posts):
#     stack = []
#     pairs = {
#         '(': ')',
#         '[': ']',
#         '{': '}'
#     }   
#     for char in posts:
#         if char in pairs:
#             stack.append(char)
#         if len(stack) != 0:
#             if pairs[stack[-1]] == char:
#                 stack.pop()
#         else:
#             return False
#         # if it's an opening char, push to stack
#         # if stack is not empty and char is a matching closing car, pop
#         # else return False. Because if char is not empty, then it needs to have a matching closing char.
        
#     return len(stack) == 0

# print(is_valid_post_format("()c"))
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))

# Problem 2: Reverse User Comments Queue
def reverse_comments_queue(comments):
    stack = []
    output = []
    for comment in comments:
        stack.append(comment)
    while stack:
        output.append(stack.pop())
    return output

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# # Problem 3: Check Symmetry in Post Titles
# def is_symmetrical_title(title):
#   pass

# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 

# # Problem 4: Engagement Boost
# def engagement_boost(engagements):
#     squared_engagements = []
    
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i]
#         squared_engagements.append((squared_engagement, i))
    
#     squared_engagements.sort(reverse=True)
    
#     result = [0] * len(engagements)
#     position = len(engagements) - 1
    
#     for square, original_index in squared_engagements:
#         result[position] = square
#         position -= 1
    
#     return result

# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))

# # Problem 5: Content Cleaner
# def clean_post(post):
#   pass

# print(clean_post("poOost")) 
# print(clean_post("abBAcC")) 
# print(clean_post("s")) 

# # Problem 6: Post Editor
# def edit_post(post):
#   pass

# print(edit_post("Boost your engagement with these tips")) 
# print(edit_post("Check out my latest vlog")) 

# # Problem 7: Post Compare
# def post_compare(draft1, draft2):
#   pass

# print(post_compare("ab#c", "ad#c"))
# print(post_compare("ab##", "c#d#")) 
# print(post_compare("a#c", "b")) 