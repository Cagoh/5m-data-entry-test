def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    if key in dct:
        print("Original dictionary: " + str(dct))
        dct[key] = value
        print("Updated dictionary: " + str(dct))
    else:
        print("Key cannot be found in dictionary:")
        print(dct)
    print()
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

def main():
    
    dct1 = update_dictionary({}, "name", "Alice")
    #print(dct1)

    dct2 = update_dictionary({"age": 25}, "age", 26)
    #print(dct2)
    

if __name__ == "__main__":
    main()