# -*- coding: utf-8 -*-
print ("Pozdravljeni v igri ugani skrito stevilo!")
skrivno_stevilo = 42

while True:
    ugani_stevilo = int(raw_input("Izberite stevilo med 1 in 100: "))
    if ugani_stevilo == skrivno_stevilo:
        print ("BRAVO USPELO TI JE!")
        break
    elif ugani_stevilo > skrivno_stevilo:
        print ("Nizje, ugani stevilo se enkrat: ")
    else:
        print ("Visje, ugani stevilo se enkrat: ")