# Day 9
q1 = input("Enter your age: ")
if int(q1) >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - int(q1)
    print("You need", years_left, "more years to learn to drive.")

# Level 2
q2 = input("Enter a month name: ").capitalize()
if q2 in ['September', 'October', 'November']:
    season = print("The season is Autumn.")
elif q2 in ['December', 'January', 'February']:
    season = print("The season is Winter.")
elif q2 in ['March', 'April', 'May']:
    season = print("The season is Spring.")
elif q2 in ['June', 'July', 'August']:
    season = print("The season is Summer.")
else:
    print("The season is invalid.")

fruits = ['banana', 'orange', 'mango', 'lemon']
q3 = input("name a fruit: ").lower()
if q3 in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(q3)
    print(fruits)

# Level 3
person={
    'first_name': 'Mii',
    'last_name': 'Wii',
    'age': 700,
    'country': 'MiiLand',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Wii Rd',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
    print("Does this Mii know Python?:", ('Python' in person['skills']))

    is_fullstack = {'React', 'Node', 'MongoDB'}
    is_backend = {'Node', 'Python', 'MongoDB'}
    is_frontend = {'JavaScript', 'React'}
    if is_fullstack.issubset(set(person['skills'])):
        print('This Mii is a fullstack developer.')
    elif is_backend.issubset(set(person['skills'])):
        print("This Mii is a backend developer.")
    elif is_frontend == set(person['skills']):
        print("This Mii is a front end developer.")
    else:
        print("unknown title!")
else:
    print("DNE")

if person['is_married'] and (person['country'] == 'MiiLand'):
    print("{} lives in MiiLand. This Mii is married.".format(person['first_name']))
else:
    print("No output.")
