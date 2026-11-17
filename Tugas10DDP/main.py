print('--------gunakan modul-----------')
import luasDatar
import kelilingDatar
luasDatar.luas_lingkaran(10)
kelilingDatar.keliling_persegi(15)
luasDatar.luas_segitiga(13, 6)

print('\n--gunakan modul dengan alias--')
import kelilingRuang as hitung
import luasRuang as ruang
hitung.keliling_kubus(3)
ruang.luas_bola(7)

print('\n--gunakan modul dgn memanggil sebagian fungsinya--')
from kelilingDatar import keliling_lingkaran
from luasRuang import luas_tabung
keliling_lingkaran(10)
luas_tabung(7, 10)

print('\n--gunakan modul dgn memanggil seluruh fungsinya--')
from luasDatar import *
from kelilingDatar import *
from kelilingRuang import *
luas_persegi(5)
keliling_segitiga(3, 4, 5)
volume_tabung(7, 10)
volume_bola(7)

print('\n--gunakan modul dgn memanggil sebagian fungsinya dengan alias--')
from luasRuang import luas_kubus as lk, luas_bola as lb
lk(3)
lb(5)