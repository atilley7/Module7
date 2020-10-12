def make_list():
    myList = []
    for x in range(3):
        val = get_input()
        if not val.isdecimal():
            raise ValueError
        elif int(val) < 1:
            raise ValueError
        elif int(val) > 50:
            raise ValueError
        else:
            myList.insert(x, int(val))

    return myList


def get_input():
    x = input("Input number : ")
    return x
