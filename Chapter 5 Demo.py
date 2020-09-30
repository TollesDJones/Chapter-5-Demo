# Mr. Jones
# This is a sample Python script Based on CH.4 material
# ASCII text generated with http://www.network-science.de/ascii/
# Donte Jones jones_donte@dublinschools.net
# IT Academy @ Emerald Campus
#
# Notes PYCHARM users: Use 'CTRL+/' keys to uncomment or comment any selected lines of code


"""
Lists

Lists are another type of sequence that is very similar to 'Tuples'
Any procedure or operator we use with Tuples will work on a list

The biggest difference between lists and Tuples is 'Lists' are Mutable

NOTES:
1. A Tuple can be concattenated another Tuple
2. You can concatenate a Tuple to a list
3. You can not concatenate a list to a Tuple

SlICING NOTES:
A slice can replace a single element or multiple
A slice does not need to replace the same number of items
A slice can replace one or more elements
"""

# A list can be created and populated using the following syntax
# Example 1
list_name = ["item1", "item2", "item3", "item4"]
#             # index 0, index 1, index 2, index 3


# # Example 2
len(list_name) # Returns 4 if using the example above

# Slicing a list works the same list_name[:] !End point is exclusive
#
# # Example 3
# # Remove Items from a list
del list_name[index]
# Deleting does not create gaps in the list indices
# All items are are re-indexed
#
# # Example 4
# # You can delete a slice from a list
del list_name[index_start:index_stop] # Remember the stop is exclusive


"""
List Methods 

Lists also have some unique methods designed to make implementation easier 
for example the: 
.append()
.remove() 
.sort() or .sort(reverse=True) for ascending and descending 
.reverse() first item becomes the last

"""

# Example 1
# High Scores
# Demonstrates list methods

scores = []

choice = None
while choice != "0":

    print(
        """
        High Scores

        0 - Exit
        1 - Show Scores
        2 - Add a Score
        3 - Remove a Score
        4 - Sort Scores
        """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # list high-score table
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)

    # add a score
    elif choice == "2":
        score = int(input("What score did you get?: "))
        scores.append(score) # Append method used to add to a list

    # remove a score
    elif choice == "3":
        score = int(input("Remove which score?: "))
        if score in scores:
            scores.remove(score) # Remove method used to remove from the list
        else:
            print(score, "isn't in the high scores list.")

    # sort scores
    elif choice == "4":
        scores.sort(reverse=True) # Reverse used to show the highest scores first

    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")


"""
Nesting Sequences 

What is a nested sequence? A sequence inside another sequence.

A list can contain other lists, tuples, strings,  or any combination of these.
Lists or tuples inside the sequence is considered a single element.
"""
#
# Example 1
nested_sequence = ["first", ("second", "third"), ["fourth", "fifth", "sixth"]]
# For example nested_sequence[1] refers to the entire Tuple at that position.

print("\nThis Tuple and all it's values are at [1]")
print(nested_sequence[1])

print("\nThis list and all it's values are at position [2]")
print(nested_sequence[2])




# ACCESSING ELEMENTS INSIDE A NESTED SEQUENCE
# Example 1
scores = [("Rob", 9000), ("Drew", 3000), ("Mark", 1500)]


# The nested elements can be assigned to a variable
a_score = scores[2]
print("a_score = sores[2] accesses all values the 3rd element of scores")
print("\n", a_score)


# We can also access the individual elements of the nested sequence
# Here we are accessing the the Tuple at index 3, and the first element
# of the Tuple.

print("\n", a_score[0])


# We can also use what is called 'Direct Access' to access any index position
# of a nested sequence.

print("\n", scores)
print("\n", scores[2][0])



# High Scores 2.0
# Demonstrates nested sequences and 'unpacking' where we assign each index of
# the nested sequence to a variable

scores = []

choice = None
while choice != "0":

    print(
        """
        High Scores 2.0

        0 - Quit
        1 - List Scores
        2 - Add a Score
        """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # display high-score table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry # each tuple has 2 items we reference them with variables 'score' and 'name'
                                # together they make the tuple refered to as 'entry'
            print(name, "\t", score)

    # add a score
    elif choice == "2":
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # keep only top 5 scores

    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")





"""
Dictionaries

A dictionary is a Python Data type that stores information in pairs 
Looking up a key will return a value associated with the key
Dictionaries are surrounded by {} curly braces 
Keys and values are separarted by a colon. 

Example
mascots = {“Ohio State”:”Buckeyes”, “Ohio University”:”Bobcats”, “Cincinnati”:“Bearcats”, “Miami”: “RedHawks”}
          { Key        : Value }
"""


# Example 1
# How to access data from a Dictionary
mascots = {"Ohio State": "Buckeye", "Ohio University":"Bobcats", "Cincinnati":"Bearcats", "Miami": "RedHawks"}
mascots["Ohio State"] # Returns "Buckeyes"

# Change a 'value' in a dictionary
mascots["Ohio State"] = "Bucks"

# Add a new key : value pair to the dictionary
mascots["Wilberforce"] = "Bull Dogs"

# Remove a key : value pair
del mascots["Ohio State"]



# Testing for a key with the 'in' operator
# Accessing keys that do not exist in the dictionary would result in an error
# Using an if statement we can avoid this
# Example 2
if "Ohio State" in mascots:
    print("Ohio State is in the mascots dictionary")
else:
    print("Key not found")


# Using the dictionaries get() method
# Example 3
print(mascots.get("Cincinnati", "Here you can specify a default message if the key can not be found"))
print()
print(mascots.get("Bowling Green", "Sorry this Key is not in the Dictionary"))




# Example 4
# Geek Translator
# Demonstrates using dictionaries

geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
        "Googling": "searching the Internet for background information on a person.",
        "Keyboard Plaque": "the collection of debris found in computer keyboards.",
        "Link Rot": "the process by which web page links become obsolete.",
        "Percussive Maintenance": "the act of striking an electronic device to make it work.",
        "Uninstalled": "being fired.  Especially popular during the dot-bomb era."}

choice = None
while choice != "0":

    print(
        """
        Geek Translator

        0 - Quit
        1 - Look Up a Geek Term
        2 - Add a Geek Term
        3 - Redefine a Geek Term
        4 - Delete a Geek Term
        """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # get a definition
    elif choice == "1":
        term = input("What term do you want me to translate?: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don't know", term)

    # add a term-definition pair
    elif choice == "2":
        term = input("What term do you want me to add?: ")
        if term not in geek:
            definition = input("\nWhat's the definition?: ")
            geek[term] = definition
            print("\n", term, "has been added.")
        else:
            print("\nThat term already exists!  Try redefining it.")

    # redefine an existing term
    elif choice == "3":
        term = input("What term do you want me to redefine?: ")
        if term in geek:
            definition = input("What's the new definition?: ")
            geek[term] = definition # Syntax for adding a term to a dictionary
            print("\n", term, "has been redefined.")
        else:
            print("\nThat term doesn't exist!  Try adding it.")

    # delete a term-definition pair
    elif choice == "4":
        term = input("What term do you want me to delete?: ")
        if term in geek:
            del geek[term] # Syntax for removing a term from a dictionary
            print("\nOkay, I deleted", term)
        else:
            print("\nI can't do that!", term, "doesn't exist in the dictionary.")

    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")