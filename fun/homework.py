def find_greatest_number(incoming_list):
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    current_largest = incoming_list[0]
    for num in incoming_list:
        if num > current_largest:
            current_largest = num
    return current_largest


def find_least_number(incoming_list):
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    current_smallest = incoming_list[0]
    for num in incoming_list:
        if num < current_smallest:
            current_smallest = num
    return current_smallest


def add_list_numbers(incoming_list):
    if incoming_list is None:
        return 0
    total = 0
    for num in incoming_list:
        total = total + num
    return total


def longest_value_key(incoming_dict):
    if incoming_dict is None:
        return None
    current_longest_value = 0
    longest_value = ""
    for key, value in incoming_dict.items():
        if len(value) > current_longest_value:
            current_longest_value = len(value)
            longest_value = value
    for key, value in incoming_dict.items():
        if value == longest_value:
            return key
