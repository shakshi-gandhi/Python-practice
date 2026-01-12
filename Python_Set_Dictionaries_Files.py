'''
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

#remove('Sanskrit_2')
#discard('Sanskrit_2') will not throw an error
#.pop()
'''

#set3 = set1.union(set2, set4)
#set3 = set1.intersection(set2)
#set3 = set1.difference(set2)
#set3 = set1.symmetric_difference(set2)

dictionary = dict(Car ='Honda CRV', Year = 2008)
#print(dictionary)

dictionary2 = {'ABC':1, 'DEF': 2}
#print(dictionary2)

#print(dictionary2.get('ABC'))
#print(dictionary2.keys())
#print(dictionary2.values())

#.pop('keyname')

for key, val in dictionary2.items():
    print(key, ":", val)

#get, values, keys, items, []

#if, elif, else

'''
day = 4
match day:
    case 1 | 2 | 3:
        print("Nothing")
    case 4:
        print('Hey')
    case _:
        print("Bye")
'''

def func(name = 'Shakshi'):
    print(name)

print(func('Not Shakshi'))
print(func())

#func(name, *greetings)
#can access greetings using [] or take n number of arguments

'''
Built in maths functions:
abs()
min()
max()
pow()
math.sqrt()
math.ceil()
math.pi()
'''

'''
import json
json.loads(x) #x is a dict
json.dumps(x) #x is json data
'''

