import math

def keliling_kubus(s):
    hasil = s ** 3
    print("keliling kubus sisi =", s, "adalah", hasil)

def keliling_tabung(r, t):
    hasil = math.pi * r ** 2 * t
    print("keliling tabung r =", r, "t =", t, "adalah", hasil)

def keliling_bola(r):
    hasil = 4 / 3 * math.pi * r ** 3
    print("keliling bola r =", r, "adalah", hasil)