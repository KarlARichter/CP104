"""
-------------------------------------------------------
[functions.py // lab10]
-------------------------------------------------------
Author:  Karl Richter
ID:       169061728
Email:   rich1728@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """

    result = next((line.strip().split(',')
                   for line in fh if line.startswith(id_number + ',')), [])
    return result


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """

    count = 0
    for line in fh:
        line = line.strip()
        if line == str(value):
            count += 1
    return count


def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    numbers = [int(line.strip()) for line in fh]
    num = max(numbers)
    fh.write(str(num) + '\n')
    return num


def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    longest_word = ""
    max_length = 0

    for line in fh:
        words = line.split()
        for word in words:
            word = word.strip()
            if len(word) >= max_length:
                max_length = len(word)
                longest_word = word

    return longest_word


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """

    for _ in range(n):
        line = fh_1.readline()
        if not line:
            break
        fh_2.write(line)
    return
