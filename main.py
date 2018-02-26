#!/usr/bin/env python3
from getpass import getpass
from hibpcheck import hibpcheck


def main():
    password = getpass()
    hibp = hibpcheck(password)
    if hibp.found:
        print('WARNING: password was FOUND!')
        print('This password appeared in the dataset ' +
              str(hibp.count) + " times")
    else:
        print('Password was not found in the dataset')


if __name__ == '__main__':
    main()
