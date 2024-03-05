def test_power(base, exponent):
    # Calculate the result of base to the power of exponent
    power_result = base ** exponent

    # Use an if statement to test if the result is greater than 5000
    if power_result > 5000:
        return True
    else:
        return False

# Example usage:
base_input = int(input("Enter the base number: "))
exponent_input = int(input("Enter the exponent number: "))

# Call the function with user-provided inputs
result = test_power(base_input, exponent_input)

# Print the result
print("Is the power greater than 5000?", result)


