# primzahlen_v2.py
# Eingabe einer Zahl >0
# Berechnen der Primzahlen aller Primzahlen mit Maximum der eingegeben Zahl
# Zeit für die Berechnung wird berechnet
# Ausgabe der Liste der gefundenen Primzahlen


import time

grenze = int(input("Obergrenze der Primzahlenausgabe: "))
 
i = 2
teiler = 0         
primzahl = [2]

start = time.time() 
 
for element in range(3, grenze):    
    while i < element:                  
        if element % i == 0:                   
            teiler = 1                 
            i = element
        else:
            i += 1
             
    i = 2
     
    if teiler == 0                  
        primzahl.append(element)
    teiler = 0                       

ende = time.time()
print('{:5.3f}s'.format(ende-start), end='  ')
     
print("Primzahlen:", primzahl)

