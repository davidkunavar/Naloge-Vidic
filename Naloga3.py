
spodnja_meja = 10
zdornja_meja = 20

stevila = []

for i in range(spodnja_meja + 1, zdornja_meja):

    stevila.append(i)

print(stevila)

print("Seštevek števil je: ")
print(sum(stevila))