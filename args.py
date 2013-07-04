#!/usr/bin/python

import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("username",
                         help="the username used to log in to the website")
    parser.add_argument("--as-boss",
                        help="visit the website as boss",
                        action="store_true")
    parser.add_argument("--login",
                        help="log in to the website",
                        action="store_true")
    parser.add_argument("--logout",
                        help="log out the website",
                        action="store_true")
    parser.add_argument("--private-mode",
                        help="tell the web site not to log this visit",
                        action="store_true")
    return parser.parse_args()
