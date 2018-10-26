def andProduct(a, b):
    x = a ^ b
    x |= (x >> 1)
    x |= (x >> 2)
    x |= (x >> 4)
    x |= (x >> 8)
    x |= (x >> 16)
    return a & ~x;

print(andProduct(1, 99999))
print(andProduct(42, 57))
print(andProduct(17, 23))
print(andProduct(11, 15))