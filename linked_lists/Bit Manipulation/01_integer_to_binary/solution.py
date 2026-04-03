def convert_integer_to_binary(n):
    if n == 0:
        return '0'
    result = ""
    while n > 0:
        if n % 2 == 1:
            result += '1'
        else:
            result += '0'
        n = n // 2
    return result[::-1]

# Example usage:
number = 10
binary_representation = convert_integer_to_binary(number)
print(f"The binary representation of {number} is: {binary_representation}")