#append list
numbers = [21, 34, 56, 99]
numbers.append(54)
print(numbers)

#extend list
prime_numbers = [2, 3, 5]
print("list1:", prime_numbers)

even_numbers = [4, 6, 8]
print("list2:", even_numbers)

prime_numbers.extend(even_numbers)
print("List after extend:", prime_numbers)
#change list

languages = ["python", "Swift", "C++"]
languages[2] = "C"
languages[0] = "Java"
languages[1] = "Rust"
print(languages)

#del item from list

capitals = ["Rome", "Riga", "Abuja", "Canberra", "Cairo", "Doha"]
del capitals[0]
del capitals[0:2]
print(capitals)

#remove item from list and iteration

family = ["Daddy", "Mommy", "Semira", "Faruk", "Bashir", "Tahira", "Camel"]
family.remove("Camel")
print(family)
for family in family:
    print(family)

family= ["Daddy", "Mommy", "Semira", "Faruk", "Bashir", "Tahira",]
print("Semira" in family)

#length
languages = ["Python", "Java", "Rust", "C++"]
print("List:", languages)
print("Total Elements:", len(languages))

numbers = {1: "one", 2: "Two", 3: "three"}
print(numbers)