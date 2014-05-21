#!/usr/bin/python

import argparse

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument("username",
                   help="the username used to visit the website")
    p.add_argument("--as-boss", action="store_true",
                   help="visit the website as boss")
    p.add_argument("--login", action="store_true",
                   help="log in to the website")
    p.add_argument("--logout", action="store_true",
                   help="log out of the website")
    p.add_argument("--view-stats", action="store_true",
                   help="view your visit statistics on the website")
    return p.parse_args()
