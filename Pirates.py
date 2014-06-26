def survivor(names, step):
    """
        >>> survivor([1,2,3,4,5,6,7,8],3)
        7
        >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 3)
        'Greg'
        >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 1)
        'Harriet'
        >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 6)
        'Andrew'
        >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 2)
        'Andrew'
        >>> survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 4)
        'Felicity'
        >>> type(survivor([1,2,3,4,5,6,7,8],3))
        <type 'int'>
        >>> type(survivor(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 3))
        <type 'str'>
        """
    
    next = step - 1 #variable "next" to store the index of first element
    while len(names)>1:# Repeat while names has more than one survivor left
        names.pop(next)# Remove the next victim from the list
        # The index of the new next victim:
        next = next + step 
        next = next - 1
        while next>len(names) - 1:
            next = next - len(names)
    return names[0]

def order(names, step):
    """
        >>> order(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 3)
        ['Craig', 'Felicity', 'Andrew', 'Edward', 'Brenda', 'Harriet', 'Deidre']
        >>> order(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 2)
        ['Brenda', 'Deidre', 'Felicity', 'Harriet', 'Craig', 'Greg', 'Edward']
        >>> order(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 4)
        ['Deidre', 'Harriet', 'Edward', 'Brenda', 'Andrew', 'Craig', 'Greg']
        >>> type(order(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 3))
        <type 'list'>
        >>> len(order(["Andrew", "Brenda", "Craig", "Deidre", "Edward", "Felicity", "Greg", "Harriet"], 3))
        7
        """
    next = step -1 #variable "next" to store the index of first element
    orders = []
    while len(names) > 1:
        orders.append(names[next])# Adding the removed victim to the new list
        names.pop(next)# Remove the next victim from the list
        # The index of the new next victim:
        next = next + step  
        next = next - 1 
        while next > (len(names)-1):
            next  = next - len(names)
    return orders

