# bucle_for_basico1.py

for num in range(101):
    print(num)

print("\n")
for num in range(2, 501, 2):
    print(num)

def contando_vanilla_ice():
    for num in range(1, 101):
        if num % 10 == 0:
            print("baby")
        elif num % 5 == 0:
            print("ice ice")
        else:
            print(num)

print("\n")
contando_vanilla_ice()

print("\n")
suma_total = 0
for num in range(0, 500001, 2):
    suma_total += num
print(suma_total)

print("\n")
for num in range(2024, 0, -3):
    print(num)

contando_vanilla_ice()

print("\n")
numInicial = 3
numFinal = 10
multiplo = 2

for num in range(numInicial, numFinal + 1):
    if num % multiplo == 0:
        print(num)