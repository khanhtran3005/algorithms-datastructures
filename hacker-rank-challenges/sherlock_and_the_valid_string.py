def isValid(s):
    characterCounter = {}
    occurenceCounter = {}

    for c in s:
        if c not in characterCounter:
            characterCounter[c] = 1
        else:
            characterCounter[c] += 1

    for value in characterCounter.values():
        if value not in occurenceCounter:
            occurenceCounter[value] = 1

        else:
            occurenceCounter[value] += 1

    if len(occurenceCounter) == 1:
        """if the number of each character in string is equal
        """
        return 'YES'

    if len(occurenceCounter) == 2:
        """if there are two differences in the number of each character
        """
        arrOccurence = list(occurenceCounter.keys())

        for key, value in occurenceCounter.items():

            if (value == 1 and abs(arrOccurence[0] - arrOccurence[1]) <= 1) \
                or key * value == 1:
                """
                1st condition: the string is valid if there is a number of characters appears once and difference between them is 1
                    E.g: aabbcceee => {2:3, 3:1} eee (3) appears once and the difference between e and others is 1
                         aaaabbbbe => {4:2, 1:1} e (1) appears once but the difference between e and others is 3

                2nd condition: if the number of characters that appear once greater than 2 ==> not valid
                    E.g: aaabbbc => {3:2, 1:1} This is the case that c (1) appears once but the differences between c and other is greater than 1.
                    However, this is still a valid case because we just need to remove c out of the string
                """
                return 'YES'
    """if the number of each character has more than 2 differences (abbccc), there is no way to fix
    """
    return 'NO'