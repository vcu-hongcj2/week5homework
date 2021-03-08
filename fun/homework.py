"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    current_largest = incoming_list[0]
    for num in incoming_list:
        if num > current_largest:
            current_largest = num
    return current_largest
    

def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    current_smallest = incoming_list[0]
    for num in incoming_list:
        if num < current_smallest:
            current_smallest = num
    return current_smallest


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    if incoming_list is None:
        return 0
    total = 0
    for num in incoming_list:
        total = total + num
    return total
        

def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    if incoming_dict is None:
        return None
    current_longest_value = 0
    longest_value = ''
    for key, value in incoming_dict.items():
        if len(value) > current_longest_value:
            current_longest_value = len(value)
            longest_value = value 
    for key, value in incoming_dict.items():
        if value == longest_value:
            return key
