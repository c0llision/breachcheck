#!/usr/bin/env python3
import requests
import hashlib
import json


class hibpEmail():
    def __init__(self, email=''):
        self.found = False
        self.count = 0

        if email:
            self.email(email)

    def email(self, email):
        self.found = False
        self.count = 0

        r = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/' +
                         email + '?truncateResponse=true')

        if r.status_code == 404:
            return False

        if r.status_code != 200:
            raise ConnectionError(
                'Error occurred quering server, got HTTP status code:',
                r.status_code)

        data = json.loads(r.text)
        self.found = True
        self.count = len(data)


class hibpPassword():
    def __init__(self, password=''):
        '''Queries HIBP for the password using k-Anonymity.
        pasword (optional): Password to query'''
        self.found = False
        self.count = 0

        if password:
            self.password(password)

    def password(self, pw):
        self.found = False
        self.count = 0

        pw_hash = hashlib.sha1(pw.encode()).hexdigest().upper()
        short_hash, long_hash = pw_hash[:5], pw_hash[5:]

        try:
            r = requests.get('https://api.pwnedpasswords.com/range/' +
                             short_hash)
        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                'Error connecting to server, check your internet connection')

        if r.status_code != 200:
            raise ConnectionError(
                'Error occurred quering server, got HTTP status code:',
                r.status_code)

        for line in r.text.split():
            breached_hash, breach_count = line.split(':')
            if breached_hash == long_hash:
                self.found = True
                self.count = int(breach_count)
                break

        return self.found
