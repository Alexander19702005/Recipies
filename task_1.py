#Задание 1
import os

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}

    for k in file:
        ingredients = []
        recepie_name = k.strip()
        #print(recepie_name)
        ingredients_count = int(file.readline())
        cook_book[recepie_name] = ingredients
        #print(ingredients_count)

        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, weight = recepie
            ingredients.append({'ingredient_name': product, 'quantity': quantity, 'measure': weight})
        file.readline()

    print(cook_book)
    #print(t)
    #print(ingredients)




