from classes.stack import Stack


def numberToBinary(number):
    s = []
    string = ""

    while number > 0:
        mod = number % 2
        s.append(mod)
        number = number // 2

    while not len(s) == 0:
        string += str(s.pop())

    return string


# print(numberToBinary(4567))
# print(numberToBinary(12345))
# print(numberToBinary(1234512345))


def baseConverter(number, base):
    DIGITS = "0123456789ABCDEF"
    s = Stack()
    string = ""

    while number > 0:
        mod = number % base
        s.push(mod)
        number = number // base

    while not s.isEmpty():
        string += DIGITS[s.pop()]

    return string


# print(baseConverter(200,2))
# print(baseConverter(233,16))
# print(baseConverter(233,8))


def recursiveBaseConverter(number, base):
    DIGITS = "0123456789ABCDEF"
    if number < base:
        return DIGITS[number]
    else:
        mod = number % base
        digit = DIGITS[mod]
        number = number // base
        return recursiveBaseConverter(number, base) + digit


# print(recursiveBaseConverter(1453,16))


def basetoNumber(string, base=2):
    arr = list(string)
    return baseToNumberHelper(arr, base)


def baseToNumberHelper(arr, base):
    DIGITS = "0123456789ABCDEF"
    num = DIGITS.index(arr.pop())

    if len(arr) == 0:
        return 0 * base + num
    else:
        return baseToNumberHelper(arr, base) * base + num


print(basetoNumber("1111111111"))
