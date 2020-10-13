import array as arr


def search_array(new_list, value):
    number_array = arr.array('i', new_list)
    for x in range(len(number_array)):
        if number_array[x] == value:
            return x
        return -1  # needs return statements to show if the value was int the list


def sort_array(new_list):
    number_array = arr.array('i', new_list)
    number_array.sort()  # needs no input , just sorts list
