Fruits_list = ['Banana', 'Apple']

#print(Fruits_list)

#print(Fruits_list[1])

new_fruits_list = list(('Cherry', 'Watermelon'))
#print(new_fruits_list)

#print(new_fruits_list[1:3])

#new_fruits_list[2] = 'Blackberry'

#Insert
Fruits_list.insert(2,"Blackberry")
Fruits_list.insert(2,"Berry")
#print(Fruits_list)
#print(new_fruits_list)

Fruits_list.append('Orange')
#print(Fruits_list)

##can extend any iterable object
Fruits_list.extend(new_fruits_list)

#print(Fruits_list)

#removing
Fruits_list.remove('Watermelon')
#print(Fruits_list)
Fruits_list.pop(2)
#print(Fruits_list)
#Fruits_list.clear()
#print(Fruits_list)

#Loops
#for x in Fruits_list:
    #print(x)

#for x in range(0, len(Fruits_list), 1):
    #print(Fruits_list[x])

#print(Fruits_list)
Fruits_list.sort()
#print(Fruits_list)
Fruits_list.sort(reverse = True)
#print(Fruits_list)
Fruits_list.reverse()
#print(Fruits_list)
a = "Shakshi".upper()
#print(a)

same_list = Fruits_list
copied_list = Fruits_list.copy()
print(copied_list)
print(copied_list == Fruits_list)
print(Fruits_list is same_list)

Fruits_list.remove("Orange")
print(Fruits_list)
print(same_list)
print(copied_list)

copied_list_v2 = Fruits_list[:]
copied_list_v3 = list(Fruits_list)
print(copied_list_v2,"\n",copied_list_v3)

print(Fruits_list.count("Watermelon"))

print(Fruits_list.index("Banana"))