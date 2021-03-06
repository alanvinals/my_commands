#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''My commands in speed!!'''

import subprocess
import sys
from argparse import ArgumentParser

__author__ = "Alan Viñals <vinals.alan@gmail.com>"
__version__ = "0.0.1"


def make_arguments_parser():
    """Build and return a command line agument parser."""
    parser = ArgumentParser(description='Collected of scripts recurrents.')
    parser.add_argument('-v',
        '--version',
        action='version',
        version=__version__)
    parser.add_argument(
        '-b',
        '--battery',
        action='store_true',
        help='show porcentage battery')
    parser.add_argument(
        '-f',
        '--firefox',
        action='store_true',
        help='open Mozilla Firefox in private mode')
    parser.add_argument(
        '--shutdown',
        action='store_true',
        help='shutdown system, default 1 hour')
    parser.add_argument(
        '--memory',
        action='store_true',
        help='show memory usage')
    parser.add_argument(
        '--mount',
        action='store_true',
        help='mount all devices')
    global args
    args = parser.parse_args()


def main():
    '''Function main'''

    make_arguments_parser()

    if len(sys.argv) < 2:
        output = "  -h, --help     show help message"
        print(output)
        exit(1)

    if args.battery:
        context = '''upower -i $(upower -e | grep 'BAT') |
                      grep -E "state|to\ full|percentage"'''
        batteryState = subprocess.getoutput(context)
        output = batteryState if batteryState else "No battery state"
        print(output)

    if args.firefox:
        subprocess.getoutput('firefox -private "https://duckduckgo.com/"')

    if args.shutdown:
        subprocess.getoutput("sudo shutdown -h 60")

    if args.memory:
        print(subprocess.getoutput("free -h --total"))

    if args.mount:
        subprocess.getoutput("sudo mount -a")
        print("All devices are mounted")

if __name__ == "__main__":
    main()
