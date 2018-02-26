#!/usr/bin/env python3
from getpass import getpass
from hibpcheck import hibpcheck


def main():
    password = getpass()
    check = hibpcheck(password)
    if check.found:
        print('WARNING: password was FOUND!')
        print('This password appeared in the dataset ' +
              str(check.count) + " times")
    else:
        print('Password was not found in the dataset')


if __name__ == '__main__':
    main()
