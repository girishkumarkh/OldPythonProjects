def dayFromDate(d, m, y):
    
    """
    >>> dayFromDate(15,10,2010)
    5
    >>> dayFromDate(1,1,2000)
    6
    >>> dayFromDate(31,12,2050)
    6
    >>> dayFromDate(1,1,10000)
    6
    >>> type(dayFromDate(15,10,2010))
    <type 'int'>
    """

    m = m - 2        
    if m < 1:
        m = m + 12
        y = y - 1
    C = y % 100       # Set C to be the Year of the Century
    D = y / 100       # Set D to be the century
    W = (13 * m - 1)/5
    X = C/4
    Y = D/4
    Z = W + X + Y + d + C - 2 * D  # setting the Z value
    day = Z % 7
    return day
