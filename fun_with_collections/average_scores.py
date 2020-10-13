def average_scores(*args, **kwargs):
    total_scores = 0

    my_str = ""
    for arg in args:
        total_scores += arg

    for key, value in kwargs.items():
        my_str += ("%s == %s" % (key, value)) + ' '

    return my_str + "Average scores :" + str(total_scores / len(args))


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
    print(average_scores(44, 55, 7, 6, first_name='Kevin', last_name='Tilley', major='Agriculture'))
    print(average_scores(5, 2, 1, 10, first_name='John', last_name='Smith', major='Computer_Science'))
