
#file creation and writing into a file
file = open("my_file.txt", 'w')

file.write("Hello, this is Hambugger practicing file handling with python.")

#file reading and display
file = open("my_file.txt", 'r')

print(file.read())

#file appending 

file = open("my_file.txt", 'a') 
file.write("\nThis is another line of code")

file = open("my_file.txt", 'r')
print(file.read())


