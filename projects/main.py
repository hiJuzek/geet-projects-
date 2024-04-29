from sys import exit

import math

done = False

while not done:

    print("kalkurwator prosty na życzenie gigachada")
    print("polecenia które obsługuje kalkurwator: + p - m / d * x sqrt s pow o ")

    liczba1 = float(input("muf jakom liczbe lubisz: "))
    znak = input("co kcesz zrobic z tymi liczbami: ")

    if znak == "end":
        done = True
    else:
        liczba2 = float(input("jakom drugom liczbe chcesz wzionsc: "))

        if znak == "+" or znak == "p":
            print(liczba1 + liczba2)
        elif znak == "-" or znak == "m":
            print(liczba1 - liczba2)
        elif znak == "/" or znak == "d":
            print(liczba1 / liczba2)
        elif znak == "*" or znak == "x":
            print(liczba1 * liczba2)
        elif znak == "sqrt" or znak == "s":
            print(math.sqrt(liczba1))
        elif znak == "pow" or znak == "o":
            print(math.pow(liczba1, liczba2))
        else:
            print("cos zjebales ewidentnie, wina na pewno nie lezy po stronie producenta kalkurwatora")