pais_x = 70000
pais_y = 180000
anos = 0

while (pais_x <= pais_y):
    pais_x *= 1.035
    pais_y *= 1.015
    anos += 1

print(anos)