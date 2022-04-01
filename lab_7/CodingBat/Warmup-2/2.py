def string_splosion(str):
    t = ""
    i = 1
    while(i <= len(str)):
        t += str[:i]
        i += 1
    return t