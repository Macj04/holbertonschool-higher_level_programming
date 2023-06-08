#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    m = 0
    try:
        for i in range(x):
            print('{}'.format(my_list[i]), end='')
            m += 1
    except Exception:
        print('', end='')
    finally:
        print('')
    return m
