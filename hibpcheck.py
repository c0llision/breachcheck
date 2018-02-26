#!/usr/bin/env python3
import requests
import hashlib


class hibpcheck():
    def __init__(self, pw=''):
        self.count = 0
        self.found = False
        if pw:
            self.password(pw)

    def password(self, pw):
        self.count = 0
        self.found = False

        pw_hash = hashlib.sha1(pw.encode()).hexdigest().upper()
        short_hash = pw_hash[:5]

        r = requests.get('https://api.pwnedpasswords.com/range/' + short_hash)

        if r.status_code != 200:
            raise Exception(
                'Error occurred quering server, got HTTP status code:',
                r.status_code)

        for line in r.text.split():
            breached_hash, breach_count = line.split(':')
            if short_hash + breached_hash == pw_hash:
                self.found = True
                self.count = int(breach_count)
                break

        return self.found
