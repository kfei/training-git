#!/usr/bin/python

import sys
from args import get_args

class Website:
    def __init__(self):
        pass

    def home(self, username):
        print 'Hello %s!' % username

if __name__ == '__main__':
    # Parsing arguments.
    args = get_args()

    # Create a website and show its contents to clients.
    w = Website()

    # Show home page to clients.
    w.home(args.username)
