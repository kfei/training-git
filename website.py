#!/usr/bin/python

import sys
from args import get_args

class Website:
    def __init__(self, username):
        self.username = username

    def home(self):
        print 'Hello %s!' % self.username

if __name__ == '__main__':
    # Parsing arguments.
    args = get_args()

    # Create a website and show its contents to clients.
    w = Website(args.username)

    # Show home page to clients.
    w.home()
