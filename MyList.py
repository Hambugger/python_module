#my_list
my_list = []  #creates an empty list
my_list.append(10) #adds values to the list
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15) #inserts value 15 to the second position to the list
my_list.extend([50, 60, 70]) #extends my_list with another list
my_list.remove(70) #removes the last element from the list
my_list.sort() #sorts my_list in an ascending order
index_30 = my_list.index(30) #find the index of value 30

#prints out the value of all
print("sorted list:", my_list)
print("Index of 30 in my_list:", index_30)
print(my_list)