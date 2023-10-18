def hex2base64(hex_string):
    mapping_array = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    hex_integer = int(hex_string, 16)
    binary_string = bin(hex_integer)
    binary_string = binary_string[2:]
    binary_string = binary_string.rjust(int(len(binary_string) / 8 + 1) * 8, '0')
    binary_string = binary_string.ljust(int(len(binary_string) / 6 + 1) * 6, '0')
    result = ''
    for i in range(int(len(binary_string) / 6)):
        actual_block_in_integer = int(binary_string[i * 6:(i + 1) * 6], base=2)
        if i == (int(len(binary_string) / 6) - 1) and actual_block_in_integer == 0:
            result = result.ljust(int(len(result) / 4) * 4, '=')
            return result
        result += mapping_array[actual_block_in_integer]

    result = result.ljust(int(len(result) / 4 + 1) * 4, '=')
    return result
