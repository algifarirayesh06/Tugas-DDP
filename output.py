awal = 1
akhir = 20

total = 0
deret = []

for i in range(awal, akhir + 1):
    if i % 2 != 0:
        deret.append(str(i))
        total += i

print(" + ".join(deret) + f" = {total}")