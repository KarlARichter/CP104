"""
------------------------------------------------------------------------
[functions.py//Assignment08]
------------------------------------------------------------------------
Author: Karl Richter
ID:     169061728
Email:  rich1728@wlu.ca
__updated__ = "2023-11-12"
------------------------------------------------------------------------
"""


def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """

    spaced = ''
    uppr = True

    for char in sentence:
        if char.isupper():
            if not uppr:
                spaced += ' ' + char.lower()
            else:
                spaced += char
            uppr = False
        else:
            spaced += char

    return spaced.strip()


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """

    if string.endswith("s") or string.endswith("sh") or string.endswith("ch"):
        pluralized = string + "es"
    elif string.endswith("y") and not string.endswith("ay") and not string.endswith("oy"):
        pluralized = string[:-1] + "ies"
    else:
        pluralized = string + "s"

    return pluralized


def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """

    i = len(str1) - 1
    j = len(str2) - 1
    suffix = ""

    while i >= 0 and j >= 0 and str1[i].lower() == str2[j].lower():
        suffix = str1[i] + suffix
        i -= 1
        j -= 1
    return suffix


def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """

    is_valid = True

    if len(isbn) != 17:
        is_valid = False

    groups = isbn.split('-')

    if len(groups) != 5:
        is_valid = False

    if groups[0] not in ['978', '979']:
        is_valid = False

    if not groups[-1].isdigit() or len(groups[-1]) != 1:
        is_valid = False

    for group in groups[1:4]:
        if not group.isdigit():
            is_valid = False

    return is_valid


def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    word_chain = True

    while len(words) > 1 and word_chain:
        first_word = words[0]
        next_word = words[1]
        if first_word[-1] == next_word[0]:
            words = words[1:]
        else:
            word_chain = False
    return word_chain
