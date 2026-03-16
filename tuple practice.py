"Access value 20 from the tuple"
tuple = (10,50,60,20,40,90,80,77,23)
print(tuple[3])











"Reverse the tuple"
tuple = (10,20,30,40,50,60,70,80,90,100)
# to reverse a tuple
reverse_tuple = tuple[::-1]
print("The Orignal tuple is: ", tuple)
print("The reversed tuple is: ",reverse_tuple)







"Swap two tuples in python"
tuple1 = ("Allina","Zohaib","gazala","Sharmeen","yousaf","Saleem")
tuple2 = ("Faiqa","Shuja","Fatima","Urwa","Maryam")

print("Orignal tuples are: ")
print("tuple1: ", tuple1)
print("tuple2: ", tuple2)

# Now swap the tuples
tuple1,tuple2 = tuple2, tuple1

print("New Swapped tuples are: ")
print("tuple1: ", tuple1)
print("tuple2: ", tuple2)