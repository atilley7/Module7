filename = 'student_info.txt'


def write_to_file(tuple_s):
    f = open('student_info.txt', 'a')
    f.write(tuple_s)
    f.write("\n")
    f.close()


def get_student_info(name):
    scores = []
    print("Enter Scores ", name)

    while True:

        score = int(input("Enter score, -1 to end"))
        if score == -1:
            break
        else:
            scores.append(score)

    write_to_file(str((name, scores)))


def read_from_file():
    file = open('student_info.txt')

    for line in file.readlines():
        print(line)

    file.close()


if __name__ == '__main__':
    f = open('student_info.txt', 'w')
    f.close()
    get_student_info('Tyler')
    get_student_info('Criner')
    get_student_info('Avery')
    get_student_info('Tilley')
    read_from_file()

    input("press any key to end")

