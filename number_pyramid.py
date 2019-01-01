import sys

def create_new_pyramid_row(input_list):
    i = 0
    new_row = []
    while i + 1 < len(input_list):
        new_number = input_list[i] + input_list[i+1]
        new_row.append(new_number)
        i += 1
    return new_row

def create_pyramid_vertically(input_list):

    row = input_list
    for i in range(0, len(input_list)):
        # print a row with one space characters between numbers.
        print(*row)
        row = create_new_pyramid_row(row)

if __name__ == '__main__':
    # convert strings to integers. For instance, from "1" to 1.
    given_list = [int(i) for i in sys.argv[1:]]
    create_pyramid_vertically(given_list)
