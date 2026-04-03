def binary_to_integer(binary):
    power = 0
    i = len(binary) - 1
    result = 0
    while i >= 0:
        if binary[i] == '1':
            result += 2 ** power
        power += 1
        i -= 1
    return result   

# Example usage:
binary_string = "1010"
integer_value = binary_to_integer(binary_string)
print(f"The integer value of binary string '{binary_string}' is: {integer_value}")