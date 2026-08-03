# Day 7
#joining sets
st1 = {'item1', 'item 2'}
st2 = {'item5', 'item6'}
print(st1 | st2) # union, random order since sets are unindexed
st1.update(st2)
print(st1)
#identify intersection items
set1 = {'hello', 'world'}
set2 = {'hello', 'dunkin'}
print(set1 & set2)
print(set1.intersection(set2))
#numerical methods, is subset or superset
integers = {1, 2, 3, 4, 5}
even_numbers = {2, 4}
print(even_numbers.issubset(integers))
print(integers.issuperset(even_numbers))
#difference vs symmetric difference: difference gives what the subject set HAS and the other doesnt, symmetric difference gives what the TOTAL elements in both are lacking from one another

#Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

q1 = print(len(it_companies))
it_companies.add('Twitter')
q2 = print(it_companies)
it_companies.update(['Meta', 'Nvidia'])
q3 = print(it_companies)
it_companies.pop()
q4 = print(it_companies)

#Level 2
q5 = print(A | B)
q6 = print(A & B) # what do both have - interseciton
q7 = print(A.issubset(B))
q8 = print(A.isdisjoint(B))
q9_1, q9_2 = print(A.update(B)), print(B.update(A))
q10 = print(A.symmetric_difference(B))

#Level 3
q12 = print(set(age))
q14 = 'I am a teacher and I love to inspire and teach people.'
convert_to_list = q14.split()
print(convert_to_list)
unique_words = print(set(convert_to_list)) #a set when converted CANNOT create duplicates (nonindexed, unordered, 'DISTINCT')
