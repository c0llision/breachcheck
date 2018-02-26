#!/usr/bin/env python3
import requests
import hashlib
from getpass import getpass


def query_hibp(pw):
    ''' returns number of times password appeared in dataset
    returns 0 if password was not found'''
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

    if not found:
        breach_count = 0
    else:
        breach_count = max(1, int(breach_count))

    return breach_count


def main():
    password = getpass()
    breach_count = query_hibp(password)

    if breach_count > 0:
        print('WARNING: password was FOUND!')
        print('This password appeared in the dataset ' +
              str(breach_count) + " times")
    else:
        print('Password was not found in the dataset')


if __name__ == '__main__':
    main()
