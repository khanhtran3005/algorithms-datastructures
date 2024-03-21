def oddNumbers(l, r):
    """
    Find odd numbers between 2 given numbers
    """
    first = None
    string = ""
    if l & 1:
        first = 1
    else:
        first = l + 1

    string += str(first)

    for i in range((r - l) // 2):
        first += 2
        string += "\n" + str(first)

    return string


print(oddNumbers(2, 5))
print(oddNumbers(3, 9))
print(oddNumbers(3, 8))
