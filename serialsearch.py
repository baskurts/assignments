def search(a, first: int, size: int, target):
    """Searches for a desired element in a list of elements 
    starting at a[first].

    Args:
        a (int): the list to search
        first (int): the list index at which the search will start
        size (int): the number of elements to search
        target: the element to search for

    Returns:
        int: If target appears in the list, index of the element
        that contains the target, else -1
    """
    i = 0
    found = False

    while((i < size) and not found and (i + first < len(a))):
        if (a[i + first] == target):
            found = True
        else:
            i += 1
    if (found):
        return i + first
    else:
        return -1