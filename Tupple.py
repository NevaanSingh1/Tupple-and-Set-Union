#Empty tuple
my_tupple = ()
print (my_tupple) 

my_tupple = (6,7,4,1)
print(my_tupple)

my_tupple= (6,7,4,1, "Nevaan")
print(my_tupple)

#Tupple having integers
my_tupple = (6,7,4,1, "Hello", (3.14))
print(my_tupple)

#tupple with mixed data types
my_tupple = ("N, e, v, a, a, n")
print (my_tupple [0])
print (my_tupple [1])

#Nested tuple
n_tupple = ("Hello", 1, 2, 3, 4, 5)

#Nested index
print(n_tupple[0] [3])
print(n_tupple[0][1])

#Slicing
print("Sliced_:", n_tupple[1:4])

#Itereting through a tuple
for letter in (my_tupple):
    print("Hello", letter)