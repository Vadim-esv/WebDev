def double_char(str):
    new_str = ""
    for i in range(len(str)):
        new_str = new_str + str[i] + str[i]
    return new_str

