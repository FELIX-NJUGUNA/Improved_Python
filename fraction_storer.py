def multiply_fractional_part(fractional_part, integer):
    carry = 0
    for i in range(len(fractional_part) - 1, -1, -1):
        product = fractional_part[i] * integer + carry
        fractional_part[i] = product % 10
        carry = product // 10

    return carry

def multiply_fractional_number(fractional_number, integer):
    whole_number_part = multiply_fractional_part(fractional_number, integer)
    return whole_number_part, fractional_number

# Example usage
fractional_number = [1, 4, 2, 8, 5, 7]
integer = 10
whole_number_part, fractional_number = multiply_fractional_number(fractional_number, integer)
print("Whole number part:", whole_number_part)
print("Fractional part:", fractional_number)
