def combination(chars, k):
    n = len(chars)
    data = [""] * k
    combinationHelper(chars, k, data, 0, n - 1, 0)


def combinationHelper(chars, k, data, start, end, index):
    if index == k:
        print(indent(index), toString(data))
    else:
        i = start
        # and end - i + 1 >= k - index (optional, remove redundant loops)
        # while i <= end:
        while i <= end and end - i + 1 >= k - index:
            data[index] = chars[i]
            print("start: ", start, "i: ", i, "index: ", index, indent(index), data)

            combinationHelper(chars, k, data, i + 1, end, index + 1)
            data[index] = ""
            i += 1


def toString(chars):
    return "".join(chars)


def indent(n):
    return "    " * n


combination(["a", "b", "c", "d"], 3)
