# primzahlen_v1.py
# Eingabe einer Zahl >0
# Berechnen der Primzahlen aller Primzahlen mit Maximum der eingegeben Zahl
# Zeit für die Berechnung wird berechnet
# Ausgabe der Liste der gefundenen Primzahlen


import time, datetime
l = []
modanzahl=0
x = 0
prim = int (input("Bitte geben sie eine Zahl ein: "))
ablauf = prim

now = now = datetime.datetime.now()
# print(now.strftime('%Y-%m-%d_%H%M%S'))
print(now.strftime('%H:%M:%S'))
# print(now.strftime('%d.%m.%Y'))

# print (datetime.datetime.today()) 
start = time.time() 

while prim != 1:
    while ablauf > 0:
        mod = prim % ablauf
        ablauf = ablauf - 1
        if mod == 0:
            modanzahl= modanzahl + 1
    if modanzahl == 2:
# Soll jede Primzahl ausgegeben werden, den Kommentar entfernen
#        print (prim, "ist eine Primzahl")
         l.append(prim)
    prim = prim -1
    ablauf = prim
    modanzahl = 0
 
ende = time.time()
print('{:5.3f}s'.format(ende-start), end='  ')
 
 
print ("Hier eine Liste aller Primzahlen:")
print (l)
