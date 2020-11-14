#Stephen Bowen 2020

def display_list(SortOrder, foodList):
    print(SortOrder)
    print(*foodList, sep='\n')

foods = ['pizza','salad','hamburger','steak','apple','orange']

display_list("foods in original order:", foods)

foods.sort()
display_list("foods in ascending alphabetical order:", foods)

foods.sort(reverse=True)
display_list("foods in descending alphabetical order:", foods)

foods2 = sorted(foods)
display_list("foods2 in ascending alphabetical order:", foods2)
display_list("foods still in descending alphabetical order:", foods)

foods.reverse()
display_list("foods in ascending alphabetical order:", foods)

foods.append('carrots')
foods.append('milk')
display_list("sorted foods with carrots and milk appended to end:", foods)

foods.sort()
display_list("foods in ascending alphabetical order:", foods)

pizza_index = foods.index('pizza')
print("Pizza is at {}".format(pizza_index))
foods.insert(pizza_index, 'fries')
pizza_index = foods.index('pizza')
print("Pizza is now at {}".format(pizza_index))
