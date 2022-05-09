empty_dict = {}
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person)
print(len(person))
print(person['first_name'])
person['tribe'] = 'kikuyu'
print(person)
person['country'] = 'Kenya'
print(person)
print('country' in person)
person.pop('country')
print(person)
person.popitem()
print(person)
del person['address']
print(person)
print(person.items())
print(person.clear())
del person
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
dict_copy = person.copy()
print(dict_copy)
keys = person.keys()
print(keys)
person_list = person.values()
print(person_list)

dog = {}
dog = {'name':'Simba','color':'white','Breed':'German Sherpherd','legs':'Black','age':12}
student_dict = {
    'first_name':'Lucy',
    'last_name':'Karimi',
    'gender':'female',
    'age':22,
    'skills':'Python',
    'country':'Kenya',
    'city':'Nairobi'
    
}
print(len(student_dict))
print(student_dict.values())
print(type(student_dict))
students= list(student_dict)
print(type(students))
student_dict['first_name'] = 'Annita'
print(student_dict)
student_dict['tribe'] = 'Kikuyu'
print(student_dict)
student_dict['county'] = 'Laikipia'
print(student_dict)
print(student_dict.keys())
print(student_dict.values())
print(student_dict)
print(list(student_dict))
print(student_dict.items())
print(student_dict.popitem())
print(student_dict.pop('tribe'))
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person)
del person
type(person)
#pop(key): removes the item with the specified key name:
#popitem(): removes the last item
#del: removes an item with specified key name
print(student_dict)
student_dict.pop('Annita')
print(student_dict)





