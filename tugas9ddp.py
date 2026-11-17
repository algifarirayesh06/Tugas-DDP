#Celcius ke Farenheit
def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(Celcius_to_fahrenheit(0))  # Output: 32.0
print(Celcius_to_fahrenheit(100))  # Output: 212.0

#Genap
def is_genap(number):
    return number % 2 == 0

print(is_genap(4))  # Output: True
print(is_genap(5))  # Output: False

#Lulus atau Gagal
def nilai_lulus(nilai):
    if nilai >= 80:
        return "Lulus"
    elif nilai < 80:
        return "Gagal"
    else:
        return "Gagal"

print(nilai_lulus(70))  # Output: Lulus
print(nilai_lulus(50))  # Output: Gagal

nilai(90)  # Output: Lulus
nilai(60)  # Output: Gagal
nilai(80)  # Output: Lulus

#Bilangan Ganjil
def is_ganjil(number):
    for i in range(1, number + 1):
        if i % 2 != 0:
            print(i, end=" ")

is_ganjil(20)  # Output: 1 3 5 7 9 11 13 15 17 19