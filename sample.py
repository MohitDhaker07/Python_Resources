"""
text
"""


from pylint_test import count


def cap_text(text):
    '''input a string
       Output the cap'''
    return text.title()


def words_in_name():
    name = input("Enter your name: ")
    return len(name)


