"""Configure what prints should be activated."""

# Temp fix for main_1000.py:
OMIT_PRINTS = False


DEBUG_MODE = True
DEBUG_MODE2 = False  # even more detail


# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'  # Reset color to default


def debug_print(string):
    if not OMIT_PRINTS:
        if DEBUG_MODE:
            print(string)

def debug_print2(string):
    if not OMIT_PRINTS:
        if DEBUG_MODE2:
            print(string)


def rprint(text):
    if not OMIT_PRINTS:
        print(RED + text + RESET)

def gprint(text):
    if not OMIT_PRINTS:
        print(GREEN + text + RESET)

def yprint(text):
    if not OMIT_PRINTS:
        print(YELLOW + text + RESET)

def bprint(text):
    if not OMIT_PRINTS:
        print(BLUE + text + RESET)

def pprint(text):
    if not OMIT_PRINTS:
        print(PURPLE + text + RESET)

def cprint(text):
    if not OMIT_PRINTS:
        print(CYAN + text + RESET)
