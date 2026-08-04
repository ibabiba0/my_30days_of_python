#Day 8
dog = dict()
dog['name'], dog['color'], dog['breed'], dog['legs'], dog['age'] = 'Teddy', 'Gray-Brown', 'Yorkie-Bichon', 4, 11
print(dog)
student = {
    'First_Name': 'StudentName',
    'Last_Name': 'LastName',
    'Gender': 'StudentGender',
    'Age': 20,
    'Marital Status': 'Not Married',
    'Skills': ['MATLAB', 'Python', 'C'],
    'Country': 'StudentCountry',
    'City': 'StudentCity',
    'Address': 'StudentAddress'
}
q5 = print(student['Skills'])
student['Skills'].append('Java')
print(student['Skills'])
q7 = print(student.keys())
q8 = print(student.values())
q9 = print(student.items()) #converts from a dictionary to a list
student.pop('Address')
print(student)
