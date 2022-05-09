from operator import ne
empty_tuple = ()
empty_tuple = tuple()
fruits = ("Avocado","Strawberry","Banana","Plams","berries")
print(len(fruits))
print(fruits[2])
sweet_fruit = fruits[3]
print(sweet_fruit)
print(fruits[2:4])
print(fruits[-3])
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
print(all_items)
print(middle_two_items)
fruits_list = list(fruits)
print(fruits_list)
print('Banana' in fruits)
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
print('item2' in tpl )# True
new_tuple = fruits + tpl
print(new_tuple)

nw_tuple = ()
print(nw_tuple)
family = ("Paul","Isaack","Kefa","Jeremy","Shadrack","Beatrice","Ann")
print(family)
new = list(family)
print(new)
new.append("James")
print(new)
new.append("Lydiah")
print(new)
print(tuple(new))
a,b,c,d,e,f,g =  "Paul","Isaack","Kefa","Jeremy","Shadrack","Beatrice","Ann"
unpacked = a,b,c,d,e,f,g
print(unpacked)
print(type(unpacked))
x = 10
y = 20

print(f'x={x}, y={y}')

tmp = x
x = y
y = tmp

print(f'x={x}, y={y}')
r, g, *other = (192, 210, 100, 0.5)
print(r,g,*other)
vegetables = ("sukuma","cabbage","carrots","brocolli")
animal_product = ("beef","skin","milk","eggs","fur","mutton")
food_stuff_up = fruits + vegetables + animal_product
print(food_stuff_up)
food_stuff_list = list(food_stuff_up)
print(food_stuff_list)
print(food_stuff_list[7])
print(food_stuff_list[2:12])
del food_stuff_up
print('milk' in vegetables)
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Denmark' in nordic_countries)
print('Iceland' in nordic_countries)

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.
sentense = "I am a teachere and i enejoy to inspire and teach people"
print(sentense.split())

