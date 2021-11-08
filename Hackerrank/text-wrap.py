def wrap(string, max_width):
    ns = string[0]
    for i in range(1,len(string)):
        if i% max_width == 0:
            ns += '\n'
            ns += string[i]
        else:
            ns += string[i]
    return ns