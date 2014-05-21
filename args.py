#!/usr/bin/python

import argparse

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument("username",
                   help="the username used to visit the website")
    p.add_argument("--login", action="store_true",
                   help="log in to the website")
    return p.parse_args()
