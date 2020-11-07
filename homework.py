# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 08:39:35 2020

@author: marle
"""

def scalar(v1, v2):
    """Berechnet das Skalarprodukt 2er Vektoren. Die Vektoren müssen als Listen oder Tupel übergeben werden."""
    sp = 0
    for x in range(0,len(v1)):
        sp = sp + v1[x]*v2[x]
    return sp

def add_frac(Zaehler1, Nenner1, Zaehler2, Nenner2):
    """Diese Funktion addiert 2 Bruche"""
    
    import math 
    
    Nenner_neu = int((Nenner1*Nenner2) / math.gcd(Nenner1, Nenner2))
    
    Zaehler1 = Zaehler1 * (Nenner_neu/Nenner1)
    
    Zaehler2 = Zaehler2 * (Nenner_neu/Nenner2)
    
    Zaehler_neu = int(Zaehler1 + Zaehler2)
    
    Zaehler_kurz = Zaehler_neu / math.gcd(Zaehler_neu, Nenner_neu)
    
    Nenner_kurz = Nenner_neu / math.gcd(Zaehler_neu, Nenner_neu)
    
    return Zaehler_kurz, Nenner_kurz

def ethiopian_calc(Z1, Z2):
    """Diese Funktion multipliziert zwei Zahlen auf Aethiopische Art"""
    
    produkt = 0
    
    if Z1 < Z2:
        zahl_klein = Z1
        zahl_gross = Z2
    else:
        zahl_klein = Z2
        zahl_gross = Z1
        
    while zahl_klein >= 1:
        
        if zahl_klein % 2 != 0:
            produkt = produkt + zahl_gross
            
        zahl_klein = zahl_klein // 2
        zahl_gross = zahl_gross * 2
    
    return produkt