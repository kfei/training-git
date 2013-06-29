#!/usr/bin/python

import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("username",
                         help="the username used to log in to the website")
    return parser.parse_args()
