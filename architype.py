#usr/bin/python

import pandas as pd
from git import repo

import re, signal, sys, time, pdb


def handler_signal(signal, frame):
    print("\n\n [!] Out ....... \n")
    sys.exit(1)
# Ctrl + C
signal.signal(signal.SIGINT, handler_signal)

REPO_DIR = "./skale/skale-manager"

def extract(url):
def transform():
def load():


if __name__ == "__main__":
    extract()
    transform()
    load()