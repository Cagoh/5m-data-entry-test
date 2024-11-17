def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    print("List: ")
    print(lst)

    i = 0

    while i < len(lst):
        # Check for first negative number
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

def main():
    
    neg1 = find_first_negative([3, 5, -1, 7, -2, 8])
    print(f"Found first negative number: {neg1}")

    neg2 = find_first_negative([2, 10, 7, 0])
    print(f"Found first negative number: {neg2}")

if __name__ == "__main__":
    main()