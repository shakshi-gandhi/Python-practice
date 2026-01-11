Subjects_set = {'Math', 'English', 'Hindi', 'History'}
print(Subjects_set)

for x in Subjects_set:
    print(x)

print("\n", 'hindi' in Subjects_set, 'Hindi' in Subjects_set)

Subjects_set.add('Sanskrit')
print(Subjects_set)

new_list = ['Geography', 'AI']
Subjects_set.update(new_list)
print(Subjects_set)

