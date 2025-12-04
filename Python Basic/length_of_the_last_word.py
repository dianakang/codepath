def length_last_word(s:str) -> int:
    l = len(s)
    ptr_idx = l-1

    # edge case: empty string
    if len(s) == 0:
        return 0

    # 1. remove white space from end + negative index error checking
    while ptr_idx >=0 and s[ptr_idx]==" ":
        ptr_idx -= 1

    last_nonspace_index = ptr_idx

    # 2. count length of the last word
    while ptr_idx >=0 and s[ptr_idx]!=" ":
        ptr_idx -= 1
    first_space_index = ptr_idx

    return last_nonspace_index - first_space_index

# test case
if __name__ == "__main__":
    print(length_last_word("hello world"))
    print(length_last_word("hello  world  "))
    print(length_last_word("    "))
    print(length_last_word("tejas"))