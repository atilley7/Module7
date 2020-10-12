def make_list():
    myList = []
    for x in range(3):
        myList.insert(x, int(get_input()))
    return myList


def get_input():
    x = input("Input number : ")
    if not x.isdecimal():
        raise Exception('Please enter only a number')
    else:
        return x


