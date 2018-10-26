def combinations(string, k):
    chars = list(string)
    chosen = ['']*len(string)
    return combinationsHelper(chars, k, chosen)


def combinationsHelper(chars, k, chosen, index=0):
    if index == k:
        print(toString(chosen))

    else:
        for i in range(len(chars)):
            chosen.append(chars.pop(i))
            combinationsHelper(chars, k, chosen, index+1)
            chars.insert(i, chosen.pop())

def toString(chars):
    return ''.join(chars)

combinations('ABCD', 2)