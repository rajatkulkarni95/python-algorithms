# Sevenish Number
n = int(input('Enter a number : '))
sev_array = []


def Sevenish(n):
    count = 0
    total = 0
    binary_n = bin(n)
    binary_n = binary_n[2:]
    sev_array = list(binary_n)
    sev_array.reverse()
    sev_array1 = [int(x) for x in sev_array]
    for x in sev_array1:
        total = total + x * (7 ** count)
        count += 1

    print(total)


Sevenish(n)
