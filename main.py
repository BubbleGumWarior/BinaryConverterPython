def convertToBinary(number):
    if number >= 1:
        convertToBinary(number // 2)
    return number % 2


if __name__ == '__main__':
    method1 = convertToBinary(10)
    method2 = bin(10).replace("0b", "")
    method3 = "{0:b}".format(int(10))
    method4 = bin(10)[2:]
