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