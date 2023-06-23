#!/usr/bin/python3
'''Class that inherits from list'''


class MyList(list):
    ''' class '''
    def print_sorted(self):
        print(sorted(self))
