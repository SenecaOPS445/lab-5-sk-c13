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

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
