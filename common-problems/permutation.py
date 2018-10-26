def stringPermutations(string):
    return stringPermutationHelper(list(string))


def stringPermutationHelper(chars, chosen=[], result=[]):


    if len(chars) == 0 and toString(chosen) not in result:
        result.append(toString(chosen))

    for i in range(len(chars)):
        chosen.append(chars.pop(i))
        # print(i, indent(len(chosen)), toString(chars),'----', toString(chosen))

        stringPermutationHelper(chars, chosen)
        chars.insert(i, chosen.pop())

        # print(i, indent(len(chosen)), toString(chars),'++++', toString(chosen))

    return result

def toString(chars):
    return ''.join(chars)

def indent(n):
    return '    '*n

print(stringPermutations('khanh'))