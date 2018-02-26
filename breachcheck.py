#!/usr/bin/env python3
import requests
import hashlib
from getpass import getpass


def query_hibp(pw):
    ''' gets list of pwned hashes from hibp'''
    pw_hash = hashlib.sha1(pw.encode()).hexdigest().upper()
    short_hash = pw_hash[:5]

    r = requests.get('https://api.pwnedpasswords.com/range/' + short_hash)

    if r.status_code != 200:
        raise Exception('Error occurred quering server, got HTTP status code:',
                        r.status_code)

    found = False
    for line in r.text.split():
        breached_hash, breach_count = line.split(':')
        if short_hash + breached_hash == pw_hash:
            found = True
            break

    if found:
        print('WARNING: password was FOUND!')
        print('This password appeared in the dataset ' +
              breach_count + " times")
    else:
        print('Password was not found in the dataset')


def main():
    password = getpass()
    query_hibp(password)


if __name__ == '__main__':
    main()
