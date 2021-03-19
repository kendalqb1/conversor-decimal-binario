def decimal_to_binary(decimal):
    if decimal <= 0:
        return "0"
    binary = ""
    while decimal > 0:
        residue = int(decimal % 2)
        decimal = int(decimal / 2)
        binary = str(residue) + binary
    return binary

def binary_to_decimal(binary):
    position = 0
    decimal = 0
    binary = binary[::-1]
    for digit in binary:
        multiply = 2 ** position
        decimal += int(digit) * multiply
        position += 1
    return decimal