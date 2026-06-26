# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1
print(len(it_companies))

#2
it_companies.add("Twitter")
#3
it_companies.add("Nvidia")
it_companies.add("Meta")
it_companies.add("Anthropic")
it_companies.add("TSMC")
#4
it_companies.remove("Facebook")
#5
print(it_companies) # ? i don't know what they want i do
#6
print(A.union(B))
print(A.intersection(B))
#7
del it_companies
del A
del B
#8 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#9
print(A.union(B))
#10
print(A.intersection(B))
#11
print("Is A a subset of B?", A.issubset(B)) # True
#12
print("Is A and B disjoint sets?", A.isdisjoint(B))
#13
print("Symmetric difference between A and B:", A.symmetric_difference(B))
#14
del A
del B

# LEVEL 3

#1
print("Is the list bigger than the set: ", len(age) > len(set(age))) # Yeah, because set doesn't allow duplicated values, so that makes smaller the set.
string_array = "Hello everyone".split(" ")
print(string_array) # We can only have one data type
list = [1, "Hello", 1.33, 1]
list[0] = 10
list.append(1000)
list.pop(0)
list.remove(1.33)
print(list, "the index of Hello is", list.index("Hello"))


tuple_1 = ("Hello", 1, 1, 5.33)
tuple_2 = ("ByeBye", 1)
# Making a union
tuple_result = tuple_2 + tuple_1
# tuple[0] = "ByeBye"
# tuple.append("HelloWorld!") # We can't change a tuple
print(tuple_1, "the index of Hello is ", tuple_result.index("Hello"))


set_1 = {"Hello", 1, 2, 2, 3, 4} 
set_1.add("Bye")
set_1.add(1.33)
set_1.remove(1)
# set.index("Bye") # The set is un-ordered and un-indexed
set_2 = {"Hello", 1, 5, 10}
removed_item =set_2.pop()
print(removed_item)
print(set_2.intersection(set_1)) # We can make intersection
print(set_2.union(set_1)) # We join both sets, it automatically delete the duplicated values


#3
phrase = "I am a teacher and I love to inspire and teach people".split(" ")
unique_words = set(phrase)
print(len(unique_words))
