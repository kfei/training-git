#!/usr/bin/python

import sys
import argparse

class Website:
    def __init__(self):
        pass

    def index(self):
        print 'Hello world!'

if __name__ == '__main__':
    # Parsing arguments.
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    # Create a website and show its contents to clients.
    w = Website()
    w.index()
