#!/usr/bin/python

import sys
from args import get_args

class Website:
    def __init__(self, username):
        self.username = username 

    def home(self):
        print 'Hello %s!' % self.username

    def logger(self):
        with open("visit.log", "a") as log:
            log.write('User %s has visited. \n' % self.username)

    def login(self):
        print 'You are now logged in as %s' % self.username

    def logout(self):
        print 'Bye %s! You have successfully logged out.' % self.username
    
    def show_stats(self):
        with open('visit.log', 'r') as log:
            all_log = [x.strip("\n") for x in log.readlines()]
            user_log = [i for i in all_log if self.username in i]
            print 'You have visited this web site %d times.' % len(user_log)

if __name__ == '__main__':
    # Parsing arguments.
    args = get_args()

    # Create a website and show its contents to clients.
    w = Website('my dear BOSS' if args.as_boss else args.username)

    # Log this visit
    w.logger()

    # Show home page to clients.
    w.home()

    # Perform a login action
    if args.login: w.login()

    # Show user statistics
    if args.view_stats: w.show_stats()

    # Perform a logout action
    if args.logout: w.logout()
