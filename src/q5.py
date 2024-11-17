def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    print(f"Is {num} divisible by {divisor}")

    if (isinstance(num, (int,float)) and isinstance(divisor, (int,float))):
        if (divisor != 0):
            return True
    return False


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

def main():
    
    div1 = check_divisibility(10, 2)
    print(div1)

    div2 = check_divisibility(7, 3)
    print(div2)

if __name__ == "__main__":
    main()