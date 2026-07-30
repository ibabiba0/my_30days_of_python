# Day6
# Level 1
q1 = tuple()
sisters, brothers = ('sis', 'sister'), ('bro', 'brother')
siblings = sisters + brothers
q4 = print('I have', str(len(siblings)), 'siblings.')
family_members = ('father', 'mother') + siblings
q5 = print(family_members)

#Level 2
siblings = family_members[2:]
parents = family_members[:2]
fruits, vegetables, animal = ('apple', 'strawberry', 'banana'), ('asparagus', 'cilantro'), ('beef', 'pork', 'not tofu')
food_stuff_tp = fruits + vegetables + animal
q2 = print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
q3 = print(food_stuff_lt)
