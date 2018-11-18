def substrCount(n, s):
    """
    1. Build a list of tuples represent the sequence of characters [("a", 3), ("b", 2), ("c", 1)].
    2. Calculate all possibles create from each tupble
    3. Calculate how many possibles created with a different character in between

    """
    lst = []
    character = s[0]
    count = 1
    result = 0
    for i in range(1, n):
        if s[i] == character:
            count += 1
        else:
            lst.append((character, count))
            character = s[i]
            count = 1
    lst.append((character, count))

    for tpl in lst:
        """calculate all possible palindromes created from same characters that are close to each other
            E.g: aaa => 6 possibles (3*4//2 = 6)
        """
        result += tpl[1] * (tpl[1] + 1) // 2

    for i in range(1, len(lst) - 1):
        if lst[i - 1][0] == lst[i + 1][0] and lst[i][1] == 1:
            """
            check palindromes created from 3 tuples with a different character in between
            """
            result += min(lst[i - 1][1], lst[i + 1][1])

    return result