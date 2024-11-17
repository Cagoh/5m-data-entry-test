def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    print("Original list:")
    print(lst)

    for i in range(len(lst)):
        if (lst[i] == find_val):
            lst[i] = replace_val
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

def main():
    
    lst1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
    print("Replace list:")
    print(lst1)
    print()

    lst2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
    print("Replace list:")
    print(lst2)
    print()
    



if __name__ == "__main__":
    main()