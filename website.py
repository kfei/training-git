#!/usr/bin/python

import sys
import argparse

class Website:
    def __init__(self):
        pass

    def home(self, username):
        print 'Hello %s!' % username

if __name__ == '__main__':
    # Parsing arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="the username used to log in to the website")
    args = parser.parse_args()

    # Create a website and show its contents to clients.
    w = Website()
    w.home(args.username)
