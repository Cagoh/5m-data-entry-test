def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    print("Original string:")
    print(s)

    if isinstance(s, str):
        return s[::-1]
    else:
        print("Can't reverse a non-string input")
    


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

def main():
    
    str1 = string_reverse("Hello World")
    print("Reverse string:")
    print(str1)
    print()
    str2 = string_reverse("Python")
    print(str2)


    

if __name__ == "__main__":
    main()