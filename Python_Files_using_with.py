#Create file
#file = open('Python_files_trial_2.txt', 'x')

with open('Python_files_trial_2.txt', 'a') as file:
    file.write("Line 1")
    file.write("Line 2")

print("Appending ended")
with open('Python_files_trial_2.txt', 'r') as file:
    print(file.readlines())
print("Readlines ended")

#When you use with, you don't need to close the file