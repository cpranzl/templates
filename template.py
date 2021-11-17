#!/usr/bin/env python

__author__ = "Christoph Pranzl"
__copyright__ = "Copyright 2018, Christoph Pranzl"
__credits__ = ["Christoph Pranzl"]
__license__ = "GPL-2.0"
__version__ = "0.0.1"
__maintainer__ = "Christoph Pranzl"
__email__ = "christoph.pranzl@pranzl.net"
__status__ = "prototype"

"""
SYNOPSIS

    template -m MESSAGE [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    Prints a message to stdout

EXAMPLES

    template -m 'Hello,world!'

EXIT STATUS

    TODO: List exit codes

"""

import sys, os, traceback, optparse, subprocess, time
from datetime import datetime


def logwrite(message):
    """ Writes message and date to logfile """
    logfile = open('logdatei.txt', 'a')
    logfile.write(message + ' ' + datetime.utcnow().isoformat() + '\n')
    logfile.close


def main():
    """ Writes the message to stdout """
    global options, args

    if options.verbose: logwrite("VERBOSE")

    print(options.message)


if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(
            formatter=optparse.TitledHelpFormatter(),
            usage=globals()['__doc__'],
            version=globals()['__version__']
        )
        parser.add_option (
            '-m', '--message', dest='message', 
            default='Hello, World!', type='string', help='Message')
        parser.add_option (
            '-v', '--verbose', action='store_true',
            default=False, help='verbose output')
        (options, args) = parser.parse_args()
        if options.verbose: print('START: ' + datetime.utcnow().isoformat())
        main()
        if options.verbose: print('STOP : ' + datetime.utcnow().isoformat())
        if options.verbose: print('TOTAL RUNNING TIME IN MINUTES: ' + str((time.time() - start_time) / 60.0))
        sys.exit(0)
    except KeyboardInterrupt as e: # Ctrl-C
        raise e
    except SystemExit as e: # sys.exit()
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        os._exit(1)
