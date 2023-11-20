def convert_fraction_to_base16(fractional_part):
    base16_representation = []
    carry = 0
    while len(fractional_part) > 0:
        digit = fractional_part[0] * 16 + carry
        carry = digit // 16
        digit = digit % 16
        base16_representation.append(digit)
        fractional_part.pop(0)

    return base16_representation

# Example usage
fractional_part = [1, 4, 2, 8, 5, 7]
base16_representation = convert_fraction_to_base16(fractional_part)
print("Base 16 representation:", base16_representation)
