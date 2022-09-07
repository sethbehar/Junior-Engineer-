'''
Write a function that takes a list of strings an prints
them, one per line, in a rectangular frame.

Helpful hint: The longest word will dictate the width of the box.

Example
For example the list ["TAMID", "IS", "THE", "COOLEST"] gets printed as:

***********
* TAMID   *
* IS      *
* THE     *
* COOLEST *
***********
'''

def boxed_string(lst):
    # find longest string length
    longest_str = -1
    for word in lst:
        if len(word) > longest_str:
            longest_str = len(word)

    # first line of *
    print("*" * (longest_str + 4))

    for word in lst:
        space = (longest_str + 1) - len(word)    # space: space in between word and right side of box
        print("* " + word + (" " * space) + "*")

    # last line of *
    print("*" * (longest_str + 4))


