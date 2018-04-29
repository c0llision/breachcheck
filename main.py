#!/usr/bin/env python3
from getpass import getpass
from hibpcheck import hibpPassword, hibpEmail


def main():
    email = input('Email:')
    hbp = hibpEmail(email)
    if hbp.found:
        print("found")
        print (str(hbp.count))

if __name__ == '__main__':
    main()
