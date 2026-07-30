#Day 4
q1 = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(q1))

company = "Coding For All"
q4, q5, q6, q7 = print(company), print(len(company)), print(company.upper()), print(company.lower())
q9 = print(company[0:-8])
q10 = print(company.index('Coding'))
q12 = print(company.replace('Coding', 'Python'))
q13 = print(company.split())
q14 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
q14 = print(q14.split(', '))
q23 = 'You cannot end a sentence with because because because is a conjunction'
because_start, because_end = q23.find('because'), q23.rfind('because')
q23 = print(q23[:because_start] + q23[because_end+8:])
q27 = 'You cannot end a sentence with because because because is a conjunction'
q27 = print(q27.replace(' because because because', ''))
q30 = '  Coding For All    '
start, last = q30.index('Coding'), q30.index('All')
q30 = print(q30[start:last+3])
q32 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
q32 = print(' # '.join(q32))
q33 = print("I am enjoying this challenge.\nI just wonder what is next.")
q34 = print("Name\tAge\tCounty\tCity\nAsabeneh\t250\tFinland\tHelsinki")
eight, six = 8, 6
print("{} + {} = {}".format(eight, six, eight+six))
print("{} - {} = {}".format(eight, six, eight-six))
print("{} * {} = {}".format(eight, six, eight*six))
