# -*- coding: utf-8 -*-
print ("Pozdravljeni v igri ugani skrito število!")
skrivno_stevilo = "42"

ugani_stevilo = raw_input("Izberite število med 1 in 100: ")

if ugani_stevilo == skrivno_stevilo:
    print ("BRAVO USPELO TI JE!")
elif ugani_stevilo > skrivno_stevilo:
    print ("Nižje, poskusite ponovno")
elif ugani_stevilo < skrivno_stevilo:
    print ("Višje, poskusite ponovno")
