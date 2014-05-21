#!/usr/bin/python

import sys
from args import get_args

class Website:
    def __init__(self, username):
        self.username = username

    def home(self):
        print 'Hello %s!' % self.username

    def logger(self):
        with open('visit.log', 'a') as log:
            log.write('User %s has visited.\n' % self.username)
            
if __name__ == '__main__':
    # Parsing arguments.
    args = get_args()

    # Create a website and show its contents to clients.
    w = Website(args.username)

    # Log this visit
    w.logger()

    # Show home page to clients.
    w.home()
