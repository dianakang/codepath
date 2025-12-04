# input: "Hello World"
# output: "dlroW olleH"

# ex) s = "Hello"
#    list_s = "H","e","l",...
def reverse_string(s: str)-> str:
    list_s = list(s)
    l = len(list_s)
    m_idx = l // 2

    for i in range(m_idx):
        # swap i
        list_s[i], list_s[l-i-1] = list_s[l-i-1], list_s[i]
    # how to create str from list
    result = "".join(list_s)
    return result

# test case
if __name__ == "__main__":
    print(reverse_string("hello")) 
    print(reverse_string("Hello World"))