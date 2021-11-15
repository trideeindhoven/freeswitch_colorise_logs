#!/usr/bin/python3

import re
import getopt
import sys, os

def printUsage():
  print('%s <options>'%(sys.argv[0]) )
  print("Options:")
  print("-h            Print this message")
  print("-f [--file]   freeswitch log full file path")

logFile = None
try:
    opts, args = getopt.getopt(sys.argv[1:],"hf:",["file="])
except getopt.GetoptError:
  printUsage()
  sys.exit(2)
for opt, arg in opts:
  if opt == '-h':
     printUsage()
     sys.exit()
  elif opt in ("-f", "--file"):
     logFile = arg

if logFile is None or logFile == '':
    print("No freeswitch logfile specified!")
    sys.exit(1)

if not os.path.isfile(logFile):
    print("File does not exist or not authorised to read file.")
    sys.exit(1)

class colors:
    '''Colors class:
    Reset all colors with colors.reset
    Two subclasses fg for foreground and bg for background.
    Use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    Also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    '''
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'



regexprs = {
            r'^.* \[NOTICE\] .*$': colors.fg.blue,
            r'^.* \[ERR\] .*$': colors.fg.red,
            r'^.* EXECUTE \[.*$': colors.fg.green,
            r'^.* \[DEBUG\] .*$': colors.fg.yellow,
            r'^[0-9a-z]{8}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{12}\sDialplan:\s': colors.fg.lightcyan,
           }
#            r'^.*\s\[DEBUG\]\s.*\sRemote\sSDP:\n(?:.*\n)*[0-9a-z]{8}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{12}\s\n': colors.fg.yellow,

with open(logFile) as fp:
    for line in fp:
        found = False
        for regexpr in regexprs:
            if re.search( regexpr, line, re.M|re.I):
                print(regexprs[regexpr]+line+colors.reset, end='')
                found = True
                break
        if not found:
            print(line, end='')

