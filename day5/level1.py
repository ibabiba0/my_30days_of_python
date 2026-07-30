#Day 5
#negative indexing
list = ['kentucky', 'fried', 'chicken']
print(list[::-1]) #negative step means go from right to left
print(list[-3:-1])
list.insert(0, 'i like')
print(list)
#.remove('item'), vs .pop(index)
#Level 1
q2 = ['Item1', 'Item2', 'Item3', 'Item 4', 'Item 5']
q3 = print(len(q2))
if len(q2) % 2 is 0: #if length is even
    first_value, middle_value1, middle_value2, last_value = q2[0], q2[len(q2) / 2], q2[(len(q2) / 2) + 1], q2[len(q2) - 1]
    q4 = print('The first, middle two, and last values are:', first_value, middle_value1, middle_value2, last_value)
elif len(q2) % 2 is not 0:
    first_value, middle_value, last_value = q2[0], q2[(len(q2) // 2) + 1], q2[len(q2) - 1]
    q4 = print('The first, middle, and last values are:', first_value, middle_value, last_value)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
q7 = print(it_companies)
it_companies[it_companies.index('Google')] = 'Not Gemini'
q10 = print(it_companies)
q11 = it_companies.append('Nvidia')
q12 = it_companies.insert(3, 'Meta')
if it_companies[6].isupper():
    it_companies[7] = it_companies[7].upper()
    q13 = print(it_companies)
else:
    it_companies[6] = it_companies[6].upper()
    q13 = print(it_companies)
q14 = print(it_companies + ['#; ']) # the string cant be concatenated without brackets indicating it's a list
q15 = 'Accenture' in it_companies
it_companies.sort()
q16 = print(it_companies)
it_companies.reverse()
q17 = print(it_companies)
q18 = print(it_companies[0:3])
q19 = print(it_companies[-3:])
num_of_middle_values = len(it_companies) - 6
q20 = print(it_companies[3:(3 + num_of_middle_values)])
del it_companies[0]
q21 = print(it_companies)
del it_companies[3:(3+num_of_middle_values)]
q22 = print(it_companies)
del it_companies[len(it_companies) - 1]
q23 = print(it_companies)
it_companies.clear()
q24 = it_companies
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
q26 = front_end + back_end
full_stack = q26
find_redux = full_stack.index('Redux')
q27 = print(full_stack[0:find_redux] + ['Python', 'SQL'] + full_stack[find_redux+1:])
