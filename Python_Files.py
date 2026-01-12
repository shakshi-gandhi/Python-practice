#open(filename, mode)
'''
Mode can be read(r), write(w), append(a), create(x)
'''
#Create file
#file = open('Python_files_trial.txt', 'x')

#Open file in write mode and overwrite
file = open('Python_files_trial.txt', 'w')
file.write('')

#Open file in append mode
file = open('Python_files_trial.txt', 'a')
print("Executing append operation.")
file.write('This is for testing if code works!')
file.write('This is line 2.')
file.close()
print("Executing close operation after append.")

#Open file in read mode
file = open('Python_files_trial.txt','r')
print("Executing read operation.")
print(file.read())
print("\nExecuting readline operation.")
print(file.readline())
file.close()
print("Executing close operation after read.")