#!/usr/bin/env python3
# Author ID: Msaeidi7

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # returns its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    clean_list = []
    for line in lines:
        clean_list.append(line.strip('\n'))
    return clean_list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
