#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        item = 0
        while item < x:
            print("{}".format(my_list[item]), end="")
            item += 1
        print("")
    except IndexError:
        print("")
    return item