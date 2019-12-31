# Remove half of the given array till it is sorted.
import random

poorSoul = 0
decimated_array = input(
    'Those whose judgement ought to be decided, Come Forth :')
decimated_array = decimated_array.split()
[int(x) for x in decimated_array]


def MadTitan(decimated_array):
    decimated_array1 = decimated_array[:]
    decimated_array1.sort()
    if decimated_array == decimated_array1:
        print(decimated_array)
        print('Perfectly Balanced! As all things should be.')
    else:
        for x in range(0, len(decimated_array)//2):
            poorSoul = random.choice(decimated_array)
            decimated_array.remove(poorSoul)
        MadTitan(decimated_array)


MadTitan(decimated_array)
