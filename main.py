#!/usr/bin/env python3
from getpass import getpass
from hibpcheck import hibpPassword, hibpEmail


def main():
    # email = input('Email:')
    # hbp = hibpEmail(email)
    # if hbp.found:
    #    print("found")
    #    print (str(hbp.count))
    
    password = getpass()
    hibp = hibpPassword(password)
    if hibp.found:
        print('WARNING: password was FOUND!')
        print('This password appeared in the dataset ' +
              str(hibp.count) + " times")
    else:
        print('Password was not found in the dataset')


if __name__ == '__main__':
    main()
