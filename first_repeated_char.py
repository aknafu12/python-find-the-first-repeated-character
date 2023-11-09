def first_recurring(given_string):
    """ 
        Function to find the first repeated character in a string

    """
    #Create a dictionary to store the count of characters
    counts = {}
    
    # Iterate through each character in the string
    for char in given_string:
        if char in counts:
            return char
        else:
            counts[char]=1
    
    # If no character is repeated, return none
    return None

