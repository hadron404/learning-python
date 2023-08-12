def right_justify(s):
    length = len(s)
    result = ' ' * (70-length) + s
    print(result)


right_justify("dsfsfds")
