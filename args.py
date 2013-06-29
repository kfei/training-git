#!/usr/bin/python

import argparse

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument("username",
                    help="the username used to visit the website")
    return p.parse_args()
