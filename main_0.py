def test_function(numbers):
    char_list = [chr(number) for number in numbers]
    char_string = ''.join(char_list)
    char_string = char_string.lower()
    substring = char_string[2:10] * 2
    return substring
