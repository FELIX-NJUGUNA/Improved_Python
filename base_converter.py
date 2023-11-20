def decimal_to_base_n(decimal, n, precision):
    # Convert decimal to interval representation
    lower_bound = int(decimal * 10 ** precision)
    upper_bound = lower_bound + 1

    # Convert interval representation to base n
    result = []
    while lower_bound > 0:
        digit = lower_bound % n
        result.insert(0, digit)
        lower_bound //= n

    # Ensure all digits are correct
    result = [digit if digit <= n // 2 else digit - n for digit in result]

    return result


# Example usage
decimal_value = 1 / 7
base_n_value = decimal_to_base_n(decimal_value, 8, 6)
print(base_n_value)
