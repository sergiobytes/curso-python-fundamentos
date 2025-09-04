# For: para iterables, cuando sabemos cuando termina
# While: cuando no sabemos cuando termina y necesitamos una condición de salida

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)

item = 0
while item <= len(my_list):
    print(item)
    item += 1