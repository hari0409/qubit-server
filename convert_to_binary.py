def str_to_binary(string):
    binary_list = []
    for char in string:
        binary_list.append(bin(ord(char))[2:].zfill(8))
    return "".join(binary_list)
