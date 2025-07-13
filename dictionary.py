programming_dictionary = {
    "Bug": "An error in a program that prevents the pragram from running as expected.",
    "Function": "A peace of code that you can easily call over and over again.",
}

#retriving item from the dictionary 
print(programming_dictionary["Bug"] + "\n")

#adding new item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#edit an item in dictionary
programming_dictionary["Bug"] = 123
print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])