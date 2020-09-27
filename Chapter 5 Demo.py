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
# list_name = ["item1", "item2", "item3", "item4"]
#             # index 0, index 1, index 2, index 3


# Example 2
len(list_name) # Returns 4 if using the example above

# Slicing a list works the same list_name[:] !End point is exclusive

# Example 3
# Remove Items from a list
del list_name[index]
# Deleting does not create gaps in the list indices
# All items are are re-indexed

# Example 4
# You can delete a slice from a list
del list_name[index_start:index_stop] # Remember the stop is exclusive


"""
List Methods 

Lists also have some unique methods designed to make implementation easier 
"""

# Example
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
        scores.append(score)

    # remove a score
    elif choice == "3":
        score = int(input("Remove which score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isn't in the high scores list.")

    # sort scores
    elif choice == "4":
        scores.sort(reverse=True)

    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")


