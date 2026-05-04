##############################################################################
# ASSIGNMENT GRADING DETAILS
##############################################################################
# PATTERNS

#######################################
# Patterns not yet completed

# PATT 2.4: used f-strings to concatenate and/or format strings
# PATT 4.5: wrote values into CSV format (without additional modules)
# PATT 5.7: error handling using `try: except:` blocks
# PATT 5.8: used `raise` to create an error to manage user behavior
# PATT 6.4: used a list comprehension (credit only if PATT 6.2 is complete)
# PATT 7.2: used indexing (by index or key) with a list, tuple, or dictionary
# PATT 7.3: used a dictionary for an appropriate data structure
# PATT 7.4: used a tuple where appropriate (unpacking and/or immutable data)

#######################################
# Patterns completed in this assignment

# PATT 5.2: correctly used `else:` block to control program behavior
# PATT 5.3: correctly used `elif:` block to control program behavior
# PATT 6.1: used a "switch"-type while-loop to loop until a condition happens
# PATT 6.2: used for-loop over an iterable like a list, tuple, or dictionary
# PATT 6.3: changed or added results inside a loop (e.g., incrementing/updating a value, appending to a list)
# PATT 7.1: used a list where a list is appropriate & useful

#######################################
# Patterns previously completed

# PATT 1.1: correctly assigned a value to a variable
# PATT 1.2: used good, consistent, descriptive variable-naming style
# PATT 2.1: correctly supplied an argument to a function (unnamed)
# PATT 2.2: correctly supplied an argument to a function (named)
# PATT 2.3: correctly concatenated strings (without f-strings)
# PATT 3.1: used an object method (e.g., string method) appropriately
# PATT 3.2: imported (and used) a Standard Library module
# PATT 4.1: correctly used `open()` inside a `with ... as:` block
# PATT 4.2: used `input()` to get user input
# PATT 4.3: read in values from a file
# PATT 4.4: wrote values to a file
# PATT 5.1: correctly used `if:` block to control program behavior
# PATT 5.4: correctly used basic boolean comparison operator
# PATT 5.5: correctly used boolean function (e.g., `isinstance`, `isfile`, `exists`)
# PATT 5.6: used `if:` to avoid an error that might happen based on user input
# PATT 8.1: used comments to explain/outline the steps in the code

##############################################################################
# ANTIPATTERNS

#######################################
# Antipatterns still uncleared

# ANTI 0.1.2: used structure before it was introduced (str.split() and/or list.count())

#######################################
# Antipatterns cleared in this assignment


#######################################
# Antipatterns new in this assignment

# ANTI 8.1: lack of comments where appropriate

##############################################################################
# COMMENTS

# Where'd the comments go?

# I'm concerned that we discussed the str.split() and that you should be using
# str.count() instead, but here you've doubled-down on splitting, but instead
# of using the much simpler list.count(), you're using an incrementing loop to
# perform the count. In other words, instead of simplifying the counting to
# just string counting, you've gone the other direction in making it more
# complicated.

# Also, I'm not sure what purpose the try: except: structure is serving, since
# you're already making sure the file path is valid.

##############################################################################
# STUDENT CODE BEGINS BELOW


import os


current_place = os.getcwd()
print("\nYou are currently in this folder:")
print(current_place)
print()

print("Files and folders here:")
print(os.listdir(current_place))
print()


path_is_valid = False


while path_is_valid == False:
    user_path = input("Enter a file path or directory path to open: ")
    print()

    if os.path.exists(user_path) == True:
        path_is_valid = True
    else:
        print("Sorry, that path doesn't seem to exist. Please try again.\n")


search_word = input("Enter the word you want to count: ")
print()


case_choice = input("Should the search be case-sensitive? Enter 'yes' or 'no': ")
print()

if case_choice.lower() == "yes":
    case_sensitive = True
elif case_choice.lower() == "no":
    case_sensitive = False
else:
    print("Didn't recognize that input, defaulting to case-insensitive search.\n")
    case_sensitive = False


files_to_search = []

if os.path.isdir(user_path):
    directory_contents = os.listdir(user_path)
    for item in directory_contents:
        full_item_path = user_path + os.sep + item
        if os.path.isfile(full_item_path):
            files_to_search.append(full_item_path)
else:
    files_to_search.append(user_path)


results = []

for file_path in files_to_search:
    try:
        with open(file_path, "r") as my_file:
            content = my_file.read()

        if case_sensitive == False:
            content_to_search = content.lower()
            word_to_find = search_word.lower()
        else:
            content_to_search = content
            word_to_find = search_word

        word_list = content_to_search.split()
        total = 0
        for w in word_list:
            clean_word = w.strip(".,!?;:\"'()[]{}")
            if clean_word == word_to_find:
                total = total + 1

        just_filename = os.path.basename(file_path)
        result_line = (
            "The word '"
            + search_word
            + "' appears "
            + str(total)
            + " time(s) in: "
            + just_filename
        )
        results.append(result_line)

        print(result_line)

    except Exception as error:
        print("Could not read file: " + file_path + " — " + str(error))

print()


with open("wordcount_results.txt", "w") as save_file:
    for line in results:
        save_file.write(line + "\n")

print("All results saved to wordcount_results.txt")
