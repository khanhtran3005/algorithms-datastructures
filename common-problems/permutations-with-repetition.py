def permutationsWithRepetition(string):
    chars = list(string)
    length = len(chars)
    return permutationsWithRepetitionHelper(chars, length, ['']*length)

def permutationsWithRepetitionHelper(chars, length, chosen, index=0, result=[]):
    if index > length - 1:
        result.append(toString(chosen))
    else:
        for i in range(length):
            chosen[index] = chars[i]
            print(i, index, indent(index), chosen)
            permutationsWithRepetitionHelper(chars, length, chosen, index + 1, result)

    return result

def toString(chars):
    return ''.join(chars)

def indent(n):
    return '    '*n


print("Result: ", permutationsWithRepetition('ABC'))