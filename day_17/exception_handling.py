try:
    print(19*4)
except:
    print("There is a big problem here")    
    
    
try:
    name = input("Enter your name:")
    year_born = input("Enter your year you were born:")
    age = 2022-year_born
    print(f'Your name is {name} and you were born in {year_born} hence your age is {age}')
except TypeError:
    print("TypeError just occured")
except ValueError:
    print("A Value error just occured")
except ZeroDivisionError:
    print("A zero divison error just occured")
    
else:
    print("I usually run with a  try block")
finally:
    print("I will run this way!!")


def sum(a,b,c,d,e):
    return a,b,c,d,e
lst = [1,2,3,4,4]
print(sum(*lst))


countries = ["Kenya","Uganda","Ethiopia","Rwanda","Somlia"]
Kenya,Uganda,Ethiopia,*rest = countries
print(Kenya,Uganda,Ethiopia,rest)
numbers = [1,2,3,4,5]
one, * middle,last =numbers
print(one,middle,last)

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Lucy', 'country':'Kenya', 'city':'Nairobi', 'age':210}
print(unpacking_person_info(**dct))

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             
print(sum_all(1, 2, 3, 4, 5, 6, 7)) 

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             
print(sum_all(1, 2, 3, 4, 5, 6, 7)) 

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Lucy",
      country="Kenya", city="Nairobi", age=250))

for index, i in enumerate(countries):
    print('hi')
    if i == 'Kenya':
        print('The country {i} has been found at index {index}')
        
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)