set = {}
set_utensils = {"spoons","plates","sufuria","sieve","grinder","jug"}
print(len(set_utensils))
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
# it_companies.update("Amazon","Visa")
print(it_companies)
it_companies.remove("Amazon")
print(it_companies)
it_companies.discard("IBM")
print(it_companies)
c =A.intersection(B)
print(c)
print(A)
print(B)
d = A.union(B)
print(d)
e = A.update(B)
print(e)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True
print(whole_numbers.issubset(even_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon)  )   # False
print(python.difference(dragon))
dragon.clear()
print(dragon)
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(whole_numbers)
del whole_numbers
print(age)
new_set = set(age)
print(new_set)
