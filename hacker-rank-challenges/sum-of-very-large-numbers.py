def sumOfVeryLargeNumbers(a, b):
    aLength = len(a)
    bLength = len(b)
    result = ""

    loop = aLength if aLength > bLength else bLength
    m = 0

    for i in range(loop):
        first = 0 if i >= aLength else int(a[aLength - 1 - i])
        second = 0 if i >= bLength else int(b[bLength - 1 - i])

        temp = first + second + m
        if temp >= 10:
            temp = str(temp)[1:]
            m = 1
        else:
            m = 0

        result = str(temp) + result

    if m == 1:
        result = "1" + result
    return result


print(sumOfVeryLargeNumbers("9999", "11"))
print(sumOfVeryLargeNumbers("111", "9999"))
print(sumOfVeryLargeNumbers("123", "11"))
print(sumOfVeryLargeNumbers("123", "123"))
