def permutations(string, k):
    chars = list(string)
    chosen = ['']*len(string)
    return permutationsHelper(chars, k, chosen)


def permutationsHelper(chars, k, chosen):
    if len(chosen) == k:
        print(toString(chosen))

    else:
        for i in range(len(chars)):
            chosen.append(chars.pop(i))
            permutationsHelper(chars, k, chosen)
            chars.insert(i, chosen.pop())

def toString(chars):
    return ''.join(chars)

permutations('ABCD', 2)