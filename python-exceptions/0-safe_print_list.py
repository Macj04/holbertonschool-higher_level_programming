#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(''.join(str(my_list[i] for i in range(x))))
    except IndexError:
        pass
    finally:
        print('')
    return min(x, len(my_list))
