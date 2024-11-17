def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    
    # Check if x and y is numeric
    if (isinstance(x, (int, float)) and isinstance(y, (int, float))):

        # Swap the value of x and y using only x and y as variables.

        print("Original values.")
        print(f"x = {x}")
        print(f"y = {y}")

        x, y = y, x
        print("Swaped values.")
        print(f"x = {x}")
        print(f"y = {y}")

        print()
        
        return 
        #return x,y
    else:
        print("x and y must be numeric to swap the values.")

        print()

        return -1


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

def main():
    
    swap("Apple", 10)
    swap(9, 17)

if __name__ == "__main__":
    main()