from random import randint
import sys

sys.setrecursionlimit(4000)

def olustur(node):
    global number
    global sinir
    if number == sinir:
        return 0
    randomness = randint(1, 100)

    if(number > 500):
        if randomness > 66:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 56:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 49:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 45:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 43:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        else:
            return 0;
    else:
        if randomness > 60:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 40:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 35:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 32:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 30:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        else:
            return 0;

print("olusturulacak input case sayisini giriniz:")

for i in range(int(input())):
    print(i, " graph sinirini giriniz:")
    sinir = int(input())
    number = 1
    while (number != sinir):
        if i<10:
            out = open("input/input0" + str(i) + ".txt", "w")
        else:
            out = open("input/input" + str(i) + ".txt", "w")
        number = 1
        olustur(1)


