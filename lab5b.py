#!/usr/bin/env python3
# Author ID: sk-c13

def read_file_string(file_name):
    """
    Takes file_name as a string and returns the entire contents of the file as a string.
    """
    file = open(file_name, 'r')
    content = file.read()
    file.close()
    return content

def read_file_list(file_name):
    """
    Takes file_name as a string and returns the entire contents of the file as a list of lines
    without new-line characters.
    """
    file = open(file_name, 'r')
    lines = [line.strip() for line in file]
    file.close()
    return lines

def append_file_string(file_name, string_of_lines):
    """
    Takes two strings, appends the string to the end of the file.
    
    Args:
    - file_name (str): The name of the file to append to.
    - string_of_lines (str): The string to append to the file.
    """
    try:
        file = open(file_name, 'a')
        file.write(string_of_lines)
        file.close()
    except FileNotFoundError:
        return 'error: could not append to file'

def write_file_list(file_name, list_of_lines):
    """
    Takes a string and list, writes all items from list to file where each item is one line.
    
    Args:
    - file_name (str): The name of the file to write to.
    - list_of_lines (list): A list of strings to write to the file.
    """
    try:
        file = open(file_name, 'w')
        for line in list_of_lines:
            file.write(line + '\n')
        file.close()
    except FileNotFoundError:
        return 'error: could not write to file'

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """
    Takes two strings, reads data from first file, writes data to new file, adds line number to new file.
    
    Args:
    - file_name_read (str): The name of the file to read from.
    - file_name_write (str): The name of the file to write to (new file).
    """
    try:
        read_file = open(file_name_read, 'r')
        write_file = open(file_name_write, 'w')
        line_number = 1
        for line in read_file:
            write_file.write(f"{line_number}:{line}")
            line_number += 1
        read_file.close()
        write_file.close()
    except FileNotFoundError:
        return 'error: could not copy and add line numbers'

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    # Append string1 to file1
    result = append_file_string(file1, string1)
    if result != 'error: could not append to file':
        print(read_file_string(file1))
    else:
        print(result)
    
    # Write list1 to file2
    result = write_file_list(file2, list1)
    if result != 'error: could not write to file':
        print(read_file_string(file2))
    else:
        print(result)
    
    # Copy file2 to file3 with line numbers added
    result = copy_file_add_line_numbers(file2, file3)
    if result != 'error: could not copy and add line numbers':
        print(read_file_string(file3))
    else:
        print(result)
