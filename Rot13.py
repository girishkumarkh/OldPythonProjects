def rot13(s):
    
    """
    >>> type(rot13("bob"))
    <type 'str'>
    >>> len(rot13("foobar"))
    6
    >>> rot13("abc")
    'nop'
    >>> rot13("XYZ")
    'KLM'
    >>> rot13('5 The Parade')
    '5 Gur Cnenqr'
    >>> rot13('5 Gur Cnenqr')
    '5 The Parade'
    """

    result = ""    # Creating an empty string named result to store the encrypted text
    for char in s:     # Let char loop over each character in the input string
        if char.isalpha():          # If this char is a letter:
            char_low = char.lower() # Set char_low to be char converted to lower case
            #  this will modify the character as necessary
            if char_low <= 'm':
                dist = 13
            else:
                dist = -13
            char = chr(ord(char) + dist)
        result = result + char      # Pushing char onto the end of the result
    return result                   # Returning the encrypted text
    
